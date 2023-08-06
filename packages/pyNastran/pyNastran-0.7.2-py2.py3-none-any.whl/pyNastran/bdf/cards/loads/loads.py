# pylint: disable=C0103,R0902,R0904,R0914,W0231,R0201
"""
All static loads are defined in this file.  This includes:

 * LSEQ
 * DAREA
 * SLOAD
 * RFORCE
 * RANDPS
"""
from __future__ import (nested_scopes, generators, division, absolute_import,
                        print_function, unicode_literals)
from six.moves import zip, range

from pyNastran.bdf.field_writer_8 import set_blank_if_default
from pyNastran.bdf.cards.baseCard import BaseCard
from pyNastran.bdf.bdfInterface.assign_type import (integer, integer_or_blank,
    double, double_or_blank, components_or_blank)
from pyNastran.bdf.field_writer_8 import print_card_8
from pyNastran.bdf.field_writer_16 import print_card_16
from pyNastran.bdf.field_writer_double import print_card_double


class Load(BaseCard):
    """defines the DefaultLoad class"""
    type = 'DefLoad'

    def __init__(self, card, data):
        self.cid = None
        self.nodes = None

    def Cid(self):
        if isinstance(self.cid, int):
            return self.cid
        else:
            return self.cid.cid

    @property
    def node_ids(self):
        return self.nodeIDs()

    @node_ids.setter
    def node_ids(self, value):
        raise ValueError("You cannot set node IDs like this...modify the node objects")

    def nodeIDs(self, nodes=None):
        """returns nodeIDs for repr functions"""
        if not nodes:
            nodes = self.nodes
        if isinstance(nodes[0], int):
            return [node for node in nodes]
        else:
            return [node.nid for node in nodes]


class LoadCombination(Load):  # LOAD, DLOAD
    def __init__(self, card, data):
        Load.__init__(self, card, data)

        if card:
            #: load ID
            self.sid = integer(card, 1, 'sid')

            #: overall scale factor
            self.scale = double(card, 2, 'scale')

            #: individual scale factors (corresponds to loadIDs)
            self.scaleFactors = []

            #: individual loadIDs (corresponds to scaleFactors)
            self.loadIDs = []

            # alternating of scale factor & load set ID
            nLoads = len(card) - 3
            assert nLoads % 2 == 0
            for i in range(nLoads // 2):
                n = 2 * i + 3
                self.scaleFactors.append(double(card, n, 'scale_factor'))
                self.loadIDs.append(integer(card, n + 1, 'load_id'))
        else:
            self.sid = data[0]
            self.scale = data[1]
            self.scaleFactors = data[2]
            self.loadIDs = data[3]
            assert len(data) == 4, '%s data=%s' % (self.type, data)

    def cross_reference(self, model):
        loadIDs2 = []
        msg = ' which is required by %s=%s' % (self.type, self.sid)
        for load_id in self.loadIDs:
            loadID2 = model.Load(load_id, msg=msg)
            loadIDs2.append(loadID2)
        self.loadIDs = loadIDs2

    def LoadID(self, lid):
        if isinstance(lid, int):
            return lid
        elif isinstance(lid, list):
            return lid[0].sid
        else:
            raise NotImplementedError(lid)

    def getLoads(self):
        """
        .. note:: requires a cross referenced load
        """
        loads = []
        for allLoads in self.loadIDs:
            for load in allLoads:
                try:
                    loads += load.getLoads()
                except RuntimeError:
                    raise RuntimeError('recursion error on load=\n%s' % str(load))
            #loads += self.ID  #: :: todo:  what does this mean, was uncommented
        return loads


class LSEQ(BaseCard):  # Requires LOADSET in case control deck
    """
    Defines a sequence of static load sets

    .. todo:: how does this work...
    """
    type = 'LSEQ'

    def __init__(self, card=None, data=None, comment=''):
        if comment:
            self._comment = comment
        if card:
            self.sid = integer(card, 1, 'sid')
            self.exciteID = integer(card, 2, 'exciteID')
            self.lid = integer(card, 3, 'lid')
            self.tid = integer_or_blank(card, 4, 'tid')
            assert len(card) <= 5, 'len(LSEQ card) = %i' % len(card)
        else:
            self.sid = data[0]
            self.exciteID = data[1]
            self.lid = data[2]
            self.tid = data[3]
            raise NotImplementedError()

    def cross_reference(self, model):
        msg = ' which is required by %s=%s' % (self.type, self.sid)
        self.lid = model.Load(self.lid, msg=msg)
        if self.tid:
            self.tid = model.Table(self.tid, msg=msg)

    def LoadID(self, lid):
        if isinstance(lid, int):
            return lid
        elif isinstance(lid, list):
            return self.LoadID(lid[0])
        else:
            return lid.sid

    def getLoads(self):
        return self.lid

    def Lid(self):
        if isinstance(self.lid, int):
            return self.lid
        else:
            return self.LoadID(self.lid)

    def Tid(self):
        if self.tid is None:
            return None
        elif isinstance(self.tid, int):
            return self.tid
        return self.tid.tid

    def raw_fields(self):
        list_fields = ['LSEQ', self.sid, self.exciteID, self.Lid(), self.Tid()]
        return list_fields

    def repr_fields(self):
        return self.raw_fields()

    def write_card(self, size=8, is_double=False):
        card = self.raw_fields()
        return self.comment() + print_card_8(card)


class DAREA(BaseCard):
    """
    Defines scale (area) factors for static and dynamic loads. In dynamic
    analysis, DAREA is used in conjunction with ACSRCE, RLOADi and TLOADi
    entries.

     +-------+-----+----+----+-----+----+----+------+
     | DAREA | SID | P1 | C1 |A1   | P2 | C2 | A2   |
     +-------+-----+----+----+-----+----+----+------+
     | DAREA | 3   | 6  | 2  | 8.2 | 15 | 1  | 10.1 |
     +-------+-----+----+----+-----+----+----+------+
    """
    type = 'DAREA'

    def __init__(self, card=None, nOffset=0, data=None, comment=''):
        if comment:
            self._comment = comment
        if card:
            nOffset *= 3
            self.sid = integer(card, 1, 'sid')
            self.p = integer(card, 2 + nOffset, 'p')
            self.c = components_or_blank(card, 3 + nOffset, 'c', 0)
            self.scale = double(card, 4 + nOffset, 'scale')
        else:
            self.sid = data[0]
            self.p = data[1]
            self.c = data[2]
            self.scale = data[3]
            assert len(data) == 4, 'data = %s' % data

    def raw_fields(self):
        list_fields = ['DAREA', self.sid, self.p, self.c, self.scale]
        return list_fields

    def write_card(self, size=8, is_double=False):
        card = self.raw_fields()
        return self.comment() + print_card_8(card)


class TabularLoad(BaseCard):
    def __init__(self, card, data):
        pass


class SLOAD(Load):
    """
    Static Scalar Load

    Defines concentrated static loads on scalar or grid points.

    .. note:: Can be used in statics OR dynamics.

    If Si refers to a grid point, the load is applied to component T1 of the
    displacement coordinate system (see the CD field on the GRID entry).
    """
    type = 'SLOAD'

    def __init__(self, card=None, data=None, comment=''):
        if comment:
            self._comment = comment
            #: load ID
        self.sid = integer(card, 1, 'sid')

        nfields = len(card) - 2
        n = nfields // 2
        if nfields % 2 == 1:
            n += 1
            msg = 'Missing last magnitude on SLOAD card=%s' % card.fields()
            raise RuntimeError(msg)

        self.nids = []
        self.mags = []
        for i in range(n):
            j = 2 * i + 2
            self.nids.append(integer(card, j, 'nid' + str(i)))
            self.mags.append(double(card, j + 1, 'mag' + str(i)))

    def cross_reference(self, model):
        msg = ' which is required by %s=%s' % (self.type, self.sid)
        for (i, nid) in enumerate(self.nids):
            self.nids[i] = model.Node(nid, msg=msg)

    def Nid(self, node):
        if isinstance(node, int):
            return node
        return node.nid

    def getLoads(self):
        """
        .. todo::  not done
        """
        return []

    def raw_fields(self):
        list_fields = ['SLOAD', self.sid]
        for (nid, mag) in zip(self.nids, self.mags):
            list_fields += [self.Nid(nid), mag]
        return list_fields

    def repr_fields(self):
        return self.raw_fields()

    def write_card(self, size=8, is_double=False):
        card = self.raw_fields()
        return self.comment() + print_card_8(card)


class RFORCE(Load):
    type = 'RFORCE'

    def __init__(self, card=None, data=None, comment=''):
        if comment:
            self._comment = comment
        if card:
            self.sid = integer(card, 1, 'sid')
            self.nid = integer_or_blank(card, 2, 'nid', 0)
            self.cid = integer_or_blank(card, 3, 'cid', 0)
            self.scale = double_or_blank(card, 4, 'scale', 1.)
            self.r1 = double_or_blank(card, 5, 'r1', 0.)
            self.r2 = double_or_blank(card, 6, 'r2', 0.)
            self.r3 = double_or_blank(card, 7, 'r3', 0.)
            self.method = integer_or_blank(card, 8, 'method', 1)
            self.racc = double_or_blank(card, 9, 'racc', 0.)
            self.mb = integer_or_blank(card, 10, 'mb', 0)
            self.idrf = integer_or_blank(card, 11, 'idrf', 0)
            assert len(card) <= 12, 'len(RFORCE card) = %i' % len(card)
        else:
            self.sid = data[0]
            print("RFORCE = %s" % data)
            raise NotImplementedError(data)

    def cross_reference(self, model):
        msg = ' which is required by RFORCE sid=%s' % self.sid
        if self.nid > 0:
            self.nid = model.Node(self.nid, msg=msg)
        self.cid = model.Coord(self.cid, msg=msg)

    def Nid(self):
        if isinstance(self.nid, int):
            return self.nid
        return self.nid.nid

    def Cid(self):
        if isinstance(self.cid, int):
            return self.cid
        return self.cid.cid

    def getLoads(self):
        return [self]

    def raw_fields(self):
        list_fields = ['RFORCE', self.sid, self.Nid(), self.Cid(), self.scale,
                       self.r1, self.r2, self.r3, self.method, self.racc,
                       self.mb, self.idrf]
        return list_fields

    def repr_fields(self):
        #method = set_blank_if_default(self.method,1)
        racc = set_blank_if_default(self.racc, 0.)
        mb = set_blank_if_default(self.mb, 0)
        idrf = set_blank_if_default(self.idrf, 0)
        list_fields = ['RFORCE', self.sid, self.Nid(), self.Cid(), self.scale,
                       self.r1, self.r2, self.r3, self.method, racc,
                       mb, idrf]
        return list_fields

    def write_card(self, size=8, is_double=False):
        card = self.repr_fields()
        if size == 8:
            return self.comment() + print_card_8(card)
        if is_double:
            return self.comment() + print_card_double(card)
        return self.comment() + print_card_16(card)


class RandomLoad(BaseCard):
    def __init__(self, card, data):
        pass


class RANDPS(RandomLoad):
    r"""
    Power Spectral Density Specification

    Defines load set power spectral density factors for use in random analysis
    having the frequency dependent form:

    .. math:: S_{jk}(F) = (X+iY)G(F)
    """
    type = 'RANDPS'

    def __init__(self, card=None, data=None, comment=''):
        if comment:
            self._comment = comment
        if card:
            #: Random analysis set identification number. (Integer > 0)
            #: Defined by RANDOM in the Case Control Deck.
            self.sid = integer(card, 1, 'sid')

            #: Subcase identification number of the excited load set.
            #: (Integer > 0)
            self.j = integer(card, 2, 'j')

            #: Subcase identification number of the applied load set.
            #: (Integer >= 0; K >= J)
            self.k = integer(card, 3, 'k')

            #: Components of the complex number. (Real)
            self.x = double_or_blank(card, 4, 'x', 0.0)
            self.y = double_or_blank(card, 5, 'y', 0.0)
            #: Identification number of a TABRNDi entry that defines G(F).
            self.tid = integer_or_blank(card, 6, 'tid', 0)
            assert len(card) <= 7, 'len(RANDPS card) = %i' % len(card)
        else:
            raise NotImplementedError(data)

    def cross_reference(self, model):
        if self.tid:
            msg = ' which is required by RANDPS sid=%s' % (self.sid)
            #self.tid = model.Table(self.tid, msg=msg)
            self.tid = model.RandomTable(self.tid, msg=msg)

    def getLoads(self):
        return [self]

    def Tid(self):
        if self.tid == 0:
            return None
        elif isinstance(self.tid, int):
            return self.tid
        return self.tid.tid

    def raw_fields(self):
        list_fields = ['RANDPS', self.sid, self.j, self.k, self.x, self.y,
                       self.Tid()]
        return list_fields

    def repr_fields(self):
        return self.raw_fields()

    def write_card(self, size=8, is_double=False):
        card = self.repr_fields()
        if size == 8:
            return self.comment() + print_card_8(card)
        if is_double:
            return self.comment() + print_card_double(card)
        return self.comment() + print_card_16(card)
