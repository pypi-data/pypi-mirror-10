# pylint: disable=C0103,R0902,R0904,R0914,W0612
"""
All solid elements are defined in this file.  This includes:

 * CHEXA8
 * CHEXA20
 * CPENTA6
 * CPENTA15
 * CTETRA4
 * CTETRA10

All solid elements are SolidElement and Element objects.
"""
from __future__ import (nested_scopes, generators, division, absolute_import,
                        print_function, unicode_literals)
from six.moves import range
from numpy import dot, cross, array, matrix, zeros
from numpy.linalg import solve, norm

from pyNastran.bdf.cards.elements.elements import Element
from pyNastran.utils.mathematics import Area, gauss
from pyNastran.bdf.bdfInterface.assign_type import (integer, integer_or_blank, fields)


def volume4(n1, n2, n3, n4):
    r"""
    Gets the volume, :math:`V`, of the tetrahedron.

    .. math:: V = \frac{(a-d) \cdot \left( (b-d) \times (c-d) \right) }{6}
    """
    V = -dot((n1 - n4), cross(n2 - n4, n3 - n4)) / 6.
    return V


def area_centroid(n1, n2, n3, n4):
    """
    Gets the area, :math:`A`, and centroid of a quad.::

      1-----2
      |   / |
      | /   |
      4-----3
    """
    a = n1 - n2
    b = n2 - n4
    area1 = Area(a, b)
    c1 = (n1 + n2 + n4) / 3.

    a = n2 - n4
    b = n2 - n3
    area2 = Area(a, b)
    c2 = (n2 + n3 + n4) / 3.

    area = area1 + area2
    try:
        centroid = (c1 * area1 + c2 * area2) / area
    except FloatingPointError:
        msg = '\nc1=%r\narea1=%r\n' % (c1, area1)
        msg += 'c2=%r\narea2=%r' % (c2, area2)
        raise FloatingPointError(msg)
    return(area, centroid)


class SolidElement(Element):
    _field_map = {1: 'nid', 2:'pid'}

    def __init__(self, card, data):
        Element.__init__(self, card, data)

    def _update_field_helper(self, n, value):
        if n - 3 < len(self.nodes):
            self.nodes[n - 3] = value
        else:
            raise KeyError('Field %r=%r is an invalid %s entry.' % (n, value, self.type))

    def cross_reference(self, model):
        raise NotImplementedError('Element type=%r must implement cross_reference')

    def Eid(self):
        return self.eid

    def E(self):
        return self.pid.mid.E()

    def G(self):
        return self.pid.mid.G()

    def Nu(self):
        return self.pid.mid.Nu()

    def Volume(self):
        """
        Base volume method that should be overwritten
        """
        pass

    def Mass(self):
        """
        Calculates the mass of the solid element
        Mass = Rho * Volume
        """
        return self.Rho() * self.Volume()

    def Mid(self):
        """
        Returns the material ID as an integer
        """
        return self.pid.Mid()

    def Rho(self):
        """
        Returns the density
        """
        try:
            return self.pid.mid.rho
        except AttributeError:
            print("self.pid = %s" % (self.pid))
            print("self.pid.mid = %s" % (str(self.pid.mid)))
            raise

    def _is_same_card(self, elem, debug=False):
        if self.type != elem.type:
            return False
        fields1 = [self.eid, self.Pid()] + self.nodes
        fields2 = [elem.eid, elem.Pid()] + elem.nodes
        if debug:
            print("fields1=%s fields2=%s" % (fields1, fields2))
        return self._is_same_fields(fields1, fields2)

    def raw_fields(self):
        list_fields = [self.type, self.eid, self.Pid()] + self.node_ids
        return list_fields

    #def write_card(self, size=8, is_double=False):
        #card = self.raw_fields()
        #msg2 = self.write_card()
        ##msg1 = self.comment() + print_card_8(card)
        ##assert msg1 == msg2, 'write_card != write_card\n%s---\n%s\n%r\n%r' % (msg1, msg2, msg1, msg2)
        #return msg2

class CHEXA8(SolidElement):
    """
    +-------+-----+-----+----+----+----+----+----+----+
    | CHEXA | EID | PID | G1 | G2 | G3 | G4 | G5 | G6 |
    +-------+-----+-----+----+----+----+----+----+----+
    |       | G7  | G8  |    |    |    |    |    |    |
    +-------+-----+-----+----+----+----+----+----+----+
    """
    type = 'CHEXA'
    asterType = 'HEXA8'
    calculixType = 'C3D8'

    def write_card(self, size=8, is_double=False):
        data = [self.eid, self.Pid()] + self.node_ids
        msg = ('CHEXA   %8i%8i%8i%8i%8i%8i%8i%8i\n'
               '        %8i%8i\n' % tuple(data))
        return self.comment() + msg

    def __init__(self, card=None, data=None, comment=''):
        SolidElement.__init__(self, card, data)
        if comment:
            self._comment = comment
        if card:
            #: Element ID
            self.eid = integer(card, 1, 'eid')
            #: Property ID
            self.pid = integer(card, 2, 'pid')
            nids = [
                integer(card, 3, 'nid1'),
                integer(card, 4, 'nid2'),
                integer(card, 5, 'nid3'),
                integer(card, 6, 'nid4'),
                integer(card, 7, 'nid5'),
                integer(card, 8, 'nid6'),
                integer(card, 9, 'nid7'),
                integer(card, 10, 'nid8')
            ]
            assert len(card) == 11, 'len(CHEXA8 card) = %i' % len(card)
        else:
            self.eid = data[0]
            self.pid = data[1]
            nids = data[2:]
            assert len(data) == 10, 'len(data)=%s data=%s' % (len(data), data)
        self.prepare_node_ids(nids)
        assert len(self.nodes) == 8

    def cross_reference(self, model):
        msg = ' which is required by %s eid=%s' % (self.type, self.eid)
        self.nodes = model.Nodes(self.nodes, allowEmptyNodes=False, msg=msg)
        self.pid = model.Property(self.pid, msg=msg)

    def _verify(self, xref=False):
        eid = self.Eid()
        pid = self.Pid()
        assert isinstance(eid, int)
        assert isinstance(pid, int)
        for i, nid in enumerate(self.node_ids):
            assert isinstance(nid, int), 'nid%i is not an integer; nid=%s' %(i, nid)
        if xref:
            c = self.Centroid()
            v = self.Volume()
            assert isinstance(v, float)
            for i in range(3):
                assert isinstance(c[i], float)

    def Centroid(self):
        """
        Averages the centroids at the two faces
        """
        (n1, n2, n3, n4, n5, n6, n7, n8) = self.nodePositions()
        A1, c1 = area_centroid(n1, n2, n3, n4)
        A2, c2 = area_centroid(n5, n6, n7, n8)
        c = (c1 + c2) / 2.
        return c

    def Volume(self):
        (n1, n2, n3, n4, n5, n6, n7, n8) = self.nodePositions()
        (A1, c1) = area_centroid(n1, n2, n3, n4)
        (A2, c2) = area_centroid(n5, n6, n7, n8)
        V = (A1 + A2) / 2. * norm(c1 - c2)
        return abs(V)

    def nodeIDs(self):
        return self.node_ids

    @property
    def node_ids(self):
        return self._nodeIDs(allowEmptyNodes=False)

    @node_ids.setter
    def node_ids(self, value):
        raise ValueError("You cannot set node IDs like this...modify the node objects")


class CHEXA20(SolidElement):
    """
    +-------+-----+-----+-----+-----+-----+-----+-----+-----+
    | CHEXA | EID | PID | G1  | G2  | G3  | G4  | G5  | G6  |
    +-------+-----+-----+-----+-----+-----+-----+-----+-----+
    |       | G7  | G8  | G9  | G10 | G11 | G12 | G13 | G14 |
    +-------+-----+-----+-----+-----+-----+-----+-----+-----+
    |       | G15 | G16 | G17 | G18 | G19 | G20 |     |     |
    +-------+-----+-----+-----+-----+-----+-----+-----+-----+
    """
    type = 'CHEXA'
    asterType = 'HEXA20'
    calculixType = 'C3D20'

    def write_card(self, size=8, is_double=False):
        nodes = self.node_ids
        nodes2 = ['' if node is None else '%8i' % node for node in nodes[8:]]

        data = [self.eid, self.Pid()] + nodes[:8] + nodes2
        msg = ('CHEXA   %8i%8i%8i%8i%8i%8i%8i%8i\n'
               '        %8i%8i%8s%8s%8s%8s%8s%8s\n'
               '        %8s%8s%8s%8s%8s%8s' % tuple(data))
        return self.comment() + msg.rstrip() + '\n'

    def __init__(self, card=None, data=None, comment=''):
        SolidElement.__init__(self, card, data)

        if comment:
            self._comment = comment
        if card:
            #: Element ID
            self.eid = integer(card, 1, 'eid')
            #: Property ID
            self.pid = integer(card, 2, 'pid')
            nids = [integer(card, 3, 'nid1'), integer(card, 4, 'nid2'),
                    integer(card, 5, 'nid3'), integer(card, 6, 'nid4'),
                    integer(card, 7, 'nid5'), integer(card, 8, 'nid6'),
                    integer(card, 9, 'nid7'), integer(card, 10, 'nid8'),
                    integer_or_blank(card, 11, 'nid9'),
                    integer_or_blank(card, 12, 'nid10'),
                    integer_or_blank(card, 13, 'nid11'),
                    integer_or_blank(card, 14, 'nid12'),
                    integer_or_blank(card, 15, 'nid13'),
                    integer_or_blank(card, 16, 'nid14'),
                    integer_or_blank(card, 17, 'nid15'),
                    integer_or_blank(card, 18, 'nid16'),
                    integer_or_blank(card, 19, 'nid17'),
                    integer_or_blank(card, 20, 'nid18'),
                    integer_or_blank(card, 21, 'nid19'),
                    integer_or_blank(card, 22, 'nid20')]
            assert len(card) <= 23, 'len(CHEXA20 card) = %i' % len(card)
        else:
            self.eid = data[0]
            self.pid = data[1]
            nids = [d if d > 0 else None for d in data[2:]]
        self.prepare_node_ids(nids, allow_empty_nodes=True)
        msg = 'len(nids)=%s nids=%s' % (len(nids), nids)
        assert len(self.nodes) <= 20, msg

    def cross_reference(self, model):
        msg = ' which is required by %s eid=%s' % (self.type, self.eid)
        self.nodes = model.Nodes(self.nodes, allowEmptyNodes=True, msg=msg)
        self.pid = model.Property(self.pid, msg=msg)

    def _verify(self, xref=False):
        eid = self.Eid()
        pid = self.Pid()
        assert isinstance(eid, int)
        assert isinstance(pid, int)
        for i, nid in enumerate(self.node_ids):
            assert nid is None or isinstance(nid, int), 'nid%i is not an integer/blank; nid=%s' %(i, nid)
        if xref:
            c = self.Centroid()
            v = self.Volume()
            assert isinstance(v, float)
            for i in range(3):
                assert isinstance(c[i], float)

    def Centroid(self):
        """
        .. seealso:: CHEXA8.Centroid
        """
        (n1, n2, n3, n4, n5,
         n6, n7, n8, n9, n10,
         n11, n12, n13, n14, n15,
         n16, n17, n18, n19, n20) = self.nodePositions()
        (A1, c1) = area_centroid(n1, n2, n3, n4)
        (A2, c2) = area_centroid(n5, n6, n7, n8)
        c = (c1 + c2) / 2.
        return c

    def Volume(self):
        """
        .. seealso:: CHEXA8.Volume
        """
        (n1, n2, n3, n4, n5,
         n6, n7, n8, n9, n10,
         n11, n12, n13, n14, n15,
         n16, n17, n18, n19, n20) = self.nodePositions()
        (A1, c1) = area_centroid(n1, n2, n3, n4)
        (A2, c2) = area_centroid(n5, n6, n7, n8)
        V = (A1 + A2) / 2. * norm(c1 - c2)
        return abs(V)

    def nodeIDs(self):
        return self.node_ids

    @property
    def node_ids(self):
        return self._nodeIDs(allowEmptyNodes=True)

    @node_ids.setter
    def node_ids(self, value):
        raise ValueError("You cannot set node IDs like this...modify the node objects")


class CPENTA6(SolidElement):
    """
    +--------+-----+-----+----+----+----+----+----+----+
    | CPENTA | EID | PID | G1 | G2 | G3 | G4 | G5 | G6 |
    +--------+-----+-----+----+----+----+----+----+----+

    ::

        *----------*
       / \        / \
      / A \      / c \
      *---*-----*-----*
      V = (A1+A2)/2  * norm(c1-c2)
      C = (c1-c2)/2
    """
    type = 'CPENTA'
    asterType = 'PENTA6'
    calculixType = 'C3D6'

    def write_card(self, size=8, is_double=False):
        nodes = self.node_ids
        data = [self.eid, self.Pid()] + nodes
        msg = 'CPENTA  %8i%8i%8i%8i%8i%8i%8i%8i\n' % tuple(data)
        return self.comment() + msg

    def __init__(self, card=None, data=None, comment=''):
        SolidElement.__init__(self, card, data)

        if comment:
            self._comment = comment
        if card:
            #: Element ID
            self.eid = integer(card, 1, 'eid')
            #: Property ID
            self.pid = integer(card, 2, 'pid')
            nids = [
                integer(card, 3, 'nid1'),
                integer(card, 4, 'nid2'),
                integer(card, 5, 'nid3'),
                integer(card, 6, 'nid4'),
                integer(card, 7, 'nid5'),
                integer(card, 8, 'nid6'),
            ]
            assert len(card) == 9, 'len(CPENTA6 card) = %i' % len(card)
        else:
            self.eid = data[0]
            self.pid = data[1]
            nids = data[2:]
            assert len(data) == 8, 'len(data)=%s data=%s' % (len(data), data)
        self.prepare_node_ids(nids)
        assert len(self.nodes) == 6

    def cross_reference(self, model):
        msg = ' which is required by %s eid=%s' % (self.type, self.eid)
        self.nodes = model.Nodes(self.nodes, allowEmptyNodes=False, msg=msg)
        self.pid = model.Property(self.pid, msg=msg)

    def getFaceAreaCentroidNormal(self, nidOpposite, nid):
        nids = self.node_ids[:6]
        indx1 = nids.index(nid)
        indx2 = nids.index(nidOpposite)

        #  offset so it's easier to map the nodes with the QRG
        pack = [indx1 + 1, indx2 + 1]
        pack.sort()
        mapper = {
            # reverse points away from the element
            [1, 2]: [1, 2, 3],  # close
            [2, 3]: [1, 2, 3],
            [1, 3]: [1, 2, 3],

            [4, 5]: [4, 5, 6],  # far-reverse
            [5, 6]: [4, 5, 6],
            [4, 6]: [4, 5, 6],

            [1, 5]: [1, 2, 5, 4],  # bottom
            [2, 4]: [1, 2, 5, 4],

            [1, 6]: [1, 3, 6, 4],  # left-reverse
            [3, 4]: [1, 3, 6, 4],

            [2, 6]: [2, 5, 6, 3],  # right
            [3, 5]: [2, 3, 6, 5],
        }

        pack2 = mapper[pack]
        if len(pack2) == 3:
            (n1, n2, n3) = pack2
            faceNodeIDs = [n1, n2, n3]
            n1i = nids.index(n1 - 1)
            n2i = nids.index(n2 - 1)
            n3i = nids.index(n3 - 1)
            p1 = self.nodes[n1i].Position()
            p2 = self.nodes[n2i].Position()
            p3 = self.nodes[n3i].Position()
            a = p1 - p2
            b = p1 - p3
            centroid = (p1 + p2 + p3) / 3.
        else:
            (n1, n2, n3, n4) = pack2
            n1i = nids.index(n1 - 1)
            n2i = nids.index(n2 - 1)
            n3i = nids.index(n3 - 1)
            n4i = nids.index(n4 - 1)
            faceNodeIDs = [n1, n2, n3, n4]
            p1 = self.nodes[n1i].Position()
            p2 = self.nodes[n2i].Position()
            p3 = self.nodes[n3i].Position()
            p4 = self.nodes[n4i].Position()
            a = p1 - p3
            b = p2 - p4
            centroid = (p1 + p2 + p3 + p4) / 4.
        normal = cross(a, b)
        n = norm(normal)
        area = 0.5 * n
        return area, centroid, normal / n

    def getFaceNodesAndArea(self, nidOpposite, nid):
        nids = self.node_ids[:6]
        indx1 = nids.index(nid)
        indx2 = nids.index(nidOpposite)

        #  offset so it's easier to map the nodes with the QRG
        pack = [indx1 + 1, indx2 + 1]
        pack.sort()
        mapper = {
            # reverse points away from the element
            [1, 2]: [1, 2, 3],  # close
            [2, 3]: [1, 2, 3],
            [1, 3]: [1, 2, 3],

            [4, 5]: [4, 5, 6],  # far-reverse
            [5, 6]: [4, 5, 6],
            [4, 6]: [4, 5, 6],

            [1, 5]: [1, 2, 5, 4],  # bottom
            [2, 4]: [1, 2, 5, 4],

            [1, 6]: [1, 3, 6, 4],  # left-reverse
            [3, 4]: [1, 3, 6, 4],

            [2, 6]: [2, 5, 6, 3],  # right
            [3, 5]: [2, 3, 6, 5],
        }

        pack2 = mapper[pack]
        if len(pack2) == 3:
            (n1, n2, n3) = pack2
            faceNodeIDs = [n1, n2, n3]
            n1i = nids.index(n1 - 1)
            n2i = nids.index(n2 - 1)
            n3i = nids.index(n3 - 1)
            p1 = self.nodes[n1i].Position()
            p2 = self.nodes[n2i].Position()
            p3 = self.nodes[n3i].Position()
            a = p1 - p2
            b = p1 - p3
            A = Area(a, b)
        else:
            (n1, n2, n3, n4) = pack2
            n1i = nids.index(n1 - 1)
            n2i = nids.index(n2 - 1)
            n3i = nids.index(n3 - 1)
            n4i = nids.index(n4 - 1)
            faceNodeIDs = [n1, n2, n3, n4]
            p1 = self.nodes[n1i].Position()
            p2 = self.nodes[n2i].Position()
            p3 = self.nodes[n3i].Position()
            p4 = self.nodes[n4i].Position()
            a = p1 - p3
            b = p2 - p4
            A = Area(a, b)
        return [faceNodeIDs, A]

    def _verify(self, xref=False):
        eid = self.Eid()
        pid = self.Pid()
        nids = self.node_ids
        assert isinstance(eid, int)
        assert isinstance(pid, int)
        for i, nid in enumerate(nids):
            assert isinstance(nid, int), 'nid%i is not an integer; nid=%s' %(i, nid)
        if xref:
            c = self.Centroid()
            v = self.Volume()
            assert isinstance(v, float)
            for i in range(3):
                assert isinstance(c[i], float)

    def Centroid(self):
        (n1, n2, n3, n4, n5, n6) = self.nodePositions()
        c1 = (n1 + n2 + n3) / 3.
        c2 = (n4 + n5 + n6) / 3.
        c = (c1 + c2) / 2.
        return c

    def Volume(self):
        (n1, n2, n3, n4, n5, n6) = self.nodePositions()
        A1 = Area(n3 - n1, n2 - n1)
        A2 = Area(n6 - n4, n5 - n4)
        c1 = (n1 + n2 + n3) / 3.
        c2 = (n4 + n5 + n6) / 3.

        V = (A1 + A2) / 2. * norm(c1 - c2)
        return abs(V)

    def raw_fields(self):
        list_fields = ['CPENTA', self.eid, self.Pid()] + self._nodeIDs(allowEmptyNodes=False)
        return list_fields

    def nodeIDs(self):
        return self.node_ids

    @property
    def node_ids(self):
        return self._nodeIDs(allowEmptyNodes=False)

    @node_ids.setter
    def node_ids(self, value):
        raise ValueError("You cannot set node IDs like this...modify the node objects")


class CPENTA15(SolidElement):
    """
    +---------+-----+-----+----+-----+-----+-----+-----+-----+
    |  CPENTA | EID | PID | G1 | G2  | G3  | G4  | G5  | G6  |
    +---------+-----+-----+----+-----+-----+-----+-----+-----+
    |         | G7  | G8  | G9 | G10 | G11 | G12 | G13 | G14 |
    +---------+-----+-----+----+-----+-----+-----+-----+-----+
    |         | G15 |     |    |     |     |     |     |     |
    +---------+-----+-----+----+-----+-----+-----+-----+-----+
    """
    type = 'CPENTA'
    asterType = 'PENTA15'
    calculixType = 'C3D15'

    def write_card(self, size=8, is_double=False):
        nodes = self.node_ids
        nodes2 = ['' if node is None else '%8i' % node for node in nodes[6:]]
        data = [self.eid, self.Pid()] + nodes[:6] + nodes2
        msg = ('CPENTA  %8i%8i%8i%8i%8i%8i%8i%8i\n'
               '        %8s%8s%8s%8s%8s%8s%8s%8s\n'
               '        %8s' % tuple(data))
        return self.comment() + msg.rstrip() + '\n'

    def __init__(self, card=None, data=None, comment=''):
        SolidElement.__init__(self, card, data)

        if comment:
            self._comment = comment
        if card:
            #: Element ID
            self.eid = integer(card, 1, 'eid')
            #: Property ID
            self.pid = integer(card, 2, 'pid')
            nids = [
                integer(card, 3, 'nid1'),
                integer(card, 4, 'nid2'),
                integer(card, 5, 'nid3'),
                integer(card, 6, 'nid4'),
                integer(card, 7, 'nid5'),
                integer(card, 8, 'nid6'),
                integer_or_blank(card, 9, 'nid7'),
                integer_or_blank(card, 10, 'nid8'),
                integer_or_blank(card, 11, 'nid9'),
                integer_or_blank(card, 12, 'nid10'),
                integer_or_blank(card, 13, 'nid11'),
                integer_or_blank(card, 14, 'nid12'),
                integer_or_blank(card, 15, 'nid13'),
                integer_or_blank(card, 16, 'nid14'),
                integer_or_blank(card, 17, 'nid15'),
            ]
            assert len(card) <= 18, 'len(CPENTA15 card) = %i' % len(card)
        else:
            self.eid = data[0]
            self.pid = data[1]
            nids = [d if d > 0 else None for d in data[2:]]
            assert len(data) == 17, 'len(data)=%s data=%s' % (len(data), data)
        self.prepare_node_ids(nids, allow_empty_nodes=True)
        assert len(self.nodes) <= 15

    def cross_reference(self, model):
        msg = ' which is required by %s eid=%s' % (self.type, self.eid)
        self.nodes = model.Nodes(self.nodes, allowEmptyNodes=True, msg=msg)
        self.pid = model.Property(self.pid, msg=msg)

    def _verify(self, xref=False):
        eid = self.Eid()
        pid = self.Pid()
        nids = self.node_ids
        assert isinstance(eid, int)
        assert isinstance(pid, int)
        for i, nid in enumerate(nids):
            assert nid is None or isinstance(nid, int), 'nid%i is not an integer/blank; nid=%s' %(i, nid)
        if xref:
            c = self.Centroid()
            v = self.Volume()
            assert isinstance(v, float)
            for i in range(3):
                assert isinstance(c[i], float)

    def Centroid(self):
        """
        .. seealso:: CPENTA6.Centroid
        """
        (n1, n2, n3, n4, n5,
         n6, n7, n8, n9, n10,
         n11, n12, n13, n14, n15) = self.nodePositions()
        c1 = (n1 + n2 + n3) / 3.
        c2 = (n4 + n5 + n6) / 3.
        c = (c1 - c2) / 2.
        return c

    def Volume(self):
        """
        .. seealso:: CPENTA6.Volume
        """
        (n1, n2, n3, n4, n5,
         n6, n7, n8, n9, n10,
         n11, n12, n13, n14, n15) = self.nodePositions()
        A1 = Area(n3 - n1, n2 - n1)
        A2 = Area(n6 - n4, n5 - n4)
        c1 = (n1 + n2 + n3) / 3.
        c2 = (n4 + n5 + n6) / 3.

        V = (A1 + A2) / 2. * norm(c1 - c2)
        return abs(V)

    def nodeIDs(self):
        return self.node_ids

    @property
    def node_ids(self):
        return self._nodeIDs(allowEmptyNodes=True)

    @node_ids.setter
    def node_ids(self, value):
        raise ValueError("You cannot set node IDs like this...modify the node objects")


class CPYRAM5(SolidElement):
    """
    +--------+-----+-----+-----+-----+-----+-----+-----+-----+
    | CPYRAM | EID | PID | G1  | G2  | G3  | G4  | G5  |     |
    +--------+-----+-----+-----+-----+-----+-----+-----+-----+
    """
    type = 'CPYRAM'
    #asterType = 'CPYRAM5'
    #calculixType = 'C3D5'

    def write_card(self, size=8, is_double=False):
        nodes = self.node_ids
        data = [self.eid, self.Pid()] + nodes
        msg = ('CPYRAM  %8i%8i%8i%8i%8i%8i%8i' % tuple(data))
        return self.comment() + msg.rstrip() + '\n'

    def __init__(self, card=None, data=None, comment=''):
        SolidElement.__init__(self, card, data)

        if comment:
            self._comment = comment
        if card:
            #: Element ID
            self.eid = integer(card, 1, 'eid')
            #: Property ID
            self.pid = integer(card, 2, 'pid')
            nids = [integer(card, 3, 'nid1'), integer(card, 4, 'nid2'),
                    integer(card, 5, 'nid3'), integer(card, 6, 'nid4'),
                    integer(card, 7, 'nid5')]
            assert len(card) == 8, 'len(CPYRAM5 1card) = %i' % len(card)
        else:
            self.eid = data[0]
            self.pid = data[1]
            nids = [d if d > 0 else None for d in data[2:]]
        self.prepare_node_ids(nids)
        msg = 'len(nids)=%s nids=%s' % (len(nids), nids)
        assert len(self.nodes) <= 20, msg

    def cross_reference(self, model):
        msg = ' which is required by %s eid=%s' % (self.type, self.eid)
        self.nodes = model.Nodes(self.nodes, allowEmptyNodes=True, msg=msg)
        self.pid = model.Property(self.pid, msg=msg)

    def _verify(self, xref=False):
        eid = self.Eid()
        pid = self.Pid()
        nids = self.node_ids
        assert isinstance(eid, int)
        assert isinstance(pid, int)
        for i, nid in enumerate(nids):
            assert nid is None or isinstance(nid, int), 'nid%i is not an integer/blank; nid=%s' %(i, nid)
        if xref:
            c = self.Centroid()
            v = self.Volume()
            assert isinstance(v, float)
            for i in range(3):
                assert isinstance(c[i], float)

    def Centroid(self):
        """
        .. seealso:: CPYRAM5.Centroid
        """
        (n1, n2, n3, n4, n5) = self.nodePositions()
        A1, c1 = area_centroid(n1, n2, n3, n4)
        c = (c1 + n5) / 2.
        return c

    def Volume(self):
        """
        .. seealso:: CPYRAM5.Volume
        """
        (n1, n2, n3, n4, n5) = self.nodePositions()
        A1, c1 = area_centroid(n1, n2, n3, n4)
        V = A1 / 3. * norm(c1 - n5)
        return abs(V)

    def nodeIDs(self):
        return self.node_ids

    @property
    def node_ids(self):
        return self._nodeIDs(allowEmptyNodes=False)

    @node_ids.setter
    def node_ids(self, value):
        raise ValueError("You cannot set node IDs like this...modify the node objects")


class CPYRAM13(SolidElement):
    """
    +--------+-----+-----+-----+-----+-----+-----+-----+-----+
    | CPYRAM | EID | PID | G1  | G2  | G3  | G4  | G5  | G6  |
    +--------+-----+-----+-----+-----+-----+-----+-----+-----+
    |        | G7  | G8  | G9  | G10 | G11 | G12 |     |     |
    +--------+-----+-----+-----+-----+-----+-----+-----+-----+
    """
    type = 'CPYRAM'
    #asterType = 'CPYRAM13'
    #calculixType = 'C3D13'

    def write_card(self, size=8, is_double=False):
        nodes = self.node_ids
        nodes2 = ['' if node is None else '%8i' % node for node in nodes[5:]]
        data = [self.eid, self.Pid()] + nodes[:5] + nodes2
        msg = ('CPYRAM  %8i%8i%8i%8i%8i%8i%8i%8s\n'
               '        %8s%8s%8s%8s%8s%8s%s' % tuple(data))
        return self.comment() + msg.rstrip() + '\n'

    def __init__(self, card=None, data=None, comment=''):
        SolidElement.__init__(self, card, data)

        if comment:
            self._comment = comment
        if card:
            #: Element ID
            self.eid = integer(card, 1, 'eid')
            #: Property ID
            self.pid = integer(card, 2, 'pid')
            nids = [integer(card, 3, 'nid1'), integer(card, 4, 'nid2'),
                    integer(card, 5, 'nid3'), integer(card, 6, 'nid4'),
                    integer(card, 7, 'nid5'),
                    integer_or_blank(card, 8, 'nid6'),
                    integer_or_blank(card, 9, 'nid7'),
                    integer_or_blank(card, 10, 'nid8'),
                    integer_or_blank(card, 11, 'nid9'),
                    integer_or_blank(card, 12, 'nid10'),
                    integer_or_blank(card, 13, 'nid11'),
                    integer_or_blank(card, 14, 'nid12'),
                    integer_or_blank(card, 15, 'nid13')]
            assert len(card) <= 16, 'len(CPYRAM13 1card) = %i' % len(card)
        else:
            self.eid = data[0]
            self.pid = data[1]
            nids = [d if d > 0 else None for d in data[2:]]
        self.prepare_node_ids(nids, allow_empty_nodes=True)
        msg = 'len(nids)=%s nids=%s' % (len(nids), nids)
        assert len(self.nodes) <= 13, msg

    def cross_reference(self, model):
        msg = ' which is required by %s eid=%s' % (self.type, self.eid)
        self.nodes = model.Nodes(self.nodes, allowEmptyNodes=True, msg=msg)
        self.pid = model.Property(self.pid, msg=msg)

    def _verify(self, xref=False):
        eid = self.Eid()
        pid = self.Pid()
        nids = self.node_ids
        assert isinstance(eid, int)
        assert isinstance(pid, int)
        for i, nid in enumerate(nids):
            assert nid is None or isinstance(nid, int), 'nid%i is not an integer/blank; nid=%s' %(i, nid)
        if xref:
            c = self.Centroid()
            v = self.Volume()
            assert isinstance(v, float)
            for i in range(3):
                assert isinstance(c[i], float)

    def Centroid(self):
        """
        .. seealso:: CPYRAM5.Centroid
        """
        (n1, n2, n3, n4, n5,
         n6, n7, n8, n9, n10,
         n11, n12, n13) = self.nodePositions()
        A1, c1 = area_centroid(n1, n2, n3, n4)
        c = (c1 + n5) / 2.
        return c

    def Volume(self):
        """
        .. seealso:: CPYRAM5.Volume
        """
        (n1, n2, n3, n4, n5,
         n6, n7, n8, n9, n10,
         n11, n12, n13) = self.nodePositions()
        A1, c1 = area_centroid(n1, n2, n3, n4)
        V = A1 / 2. * norm(c1 - n5)
        return abs(V)

    def nodeIDs(self):
        return self.node_ids

    @property
    def node_ids(self):
        return self._nodeIDs(allowEmptyNodes=True)

    @node_ids.setter
    def node_ids(self, value):
        raise ValueError("You cannot set node IDs like this...modify the node objects")


class CTETRA4(SolidElement):
    """
    +--------+-----+-----+----+----+----+----+
    | CTETRA | EID | PID | G1 | G2 | G3 | G4 |
    +--------+-----+-----+----+----+----+----+
    """
    type = 'CTETRA'
    asterType = 'TETRA4'
    calculixType = 'C3D4'

    def write_card(self, size=8, is_double=False):
        nodes = self.node_ids
        data = [self.eid, self.Pid()] + nodes
        msg = 'CTETRA  %8i%8i%8i%8i%8i%8i\n' % tuple(data)
        return self.comment() + msg

    def __init__(self, card=None, data=None, comment=''):
        SolidElement.__init__(self, card, data)
        if comment:
            self._comment = comment
        if card:
            #: Element ID
            self.eid = integer(card, 1, 'eid')
            #: Property ID
            self.pid = integer(card, 2, 'pid')
            nids = [integer(card, 3, 'nid1'),
                    integer(card, 4, 'nid2'),
                    integer(card, 5, 'nid3'),
                    integer(card, 6, 'nid4'), ]
            assert len(card) == 7, 'len(CTETRA4 card) = %i' % len(card)
        else:
            self.eid = data[0]
            self.pid = data[1]
            nids = data[2:]
            assert len(data) == 6, 'len(data)=%s data=%s' % (len(data), data)
        self.prepare_node_ids(nids)
        assert len(self.nodes) == 4

    def cross_reference(self, model):
        msg = ' which is required by %s eid=%s' % (self.type, self.eid)
        self.nodes = model.Nodes(self.nodes, allowEmptyNodes=False, msg=msg)
        self.pid = model.Property(self.pid, msg=msg)

    def _verify(self, xref=False):
        eid = self.Eid()
        pid = self.Pid()
        nids = self.node_ids
        assert isinstance(eid, int)
        assert isinstance(pid, int)
        for i, nid in enumerate(nids):
            assert isinstance(nid, int), 'nid%i is not an integer; nid=%s' %(i, nid)
        if xref:
            c = self.Centroid()
            v = self.Volume()
            assert isinstance(v, float)
            for i in range(3):
                assert isinstance(c[i], float)

    def Volume(self):
        (n1, n2, n3, n4) = self.nodePositions()
        return volume4(n1, n2, n3, n4)

    def Centroid(self):
        (n1, n2, n3, n4) = self.nodePositions()
        return (n1 + n2 + n3 + n4) / 4.

    def getFaceNodes(self, nid_opposite, nid=None):
        assert nid is None, nid
        nids = self.node_ids[:4]
        indx = nids.index(nid_opposite)
        nids.pop(indx)
        return nids

    def getFaceAreaCentroidNormal(self, nid_opposite, nid=None):
        n1, n2, n3 = self.getFaceNodes(nid_opposite)
        faceNodeIDs = [n1, n2, n3]
        p1 = self.nodes[n1].Position()
        p2 = self.nodes[n2].Position()
        p3 = self.nodes[n3].Position()
        a = p1 - p2
        b = p1 - p3
        normal = cross(a, b)
        n = norm(normal)
        A = 0.5 * n
        centroid = (p1 + p2 + p3) / 3.
        return A, centroid, normal / n

    def nodeIDs(self):
        return self.node_ids

    @property
    def node_ids(self):
        return self._nodeIDs(allowEmptyNodes=False)

    @node_ids.setter
    def node_ids(self, value):
        raise ValueError("You cannot set node IDs like this...modify the node objects")


class CTETRA10(SolidElement):
    """
    +--------+-----+-----+-----+-----+-----+----+-----+-----+
    | CTETRA | EID | PID | G1  | G2  | G3  | G4 | G5  | G6  |
    +--------+-----+-----+-----+-----+-----+----+-----+-----+
    |        | G7  |  G8 | G9  | G10 |     |    |     |     |
    +--------+-----+-----+-----+-----+-----+----+-----+-----+

    +--------+-----+-----+-----+-----+-----+----+-----+-----+
    | CTETRA | 1   | 1   | 239 | 229 | 516 | 99 | 335 | 103 |
    +--------+-----+-----+-----+-----+-----+----+-----+-----+
    |        | 265 | 334 | 101 | 102 |     |    |     |     |
    +--------+-----+-----+-----+-----+-----+----+-----+-----+
    """
    type = 'CTETRA'
    asterType = 'TETRA10'
    calculixType = 'C3D10'

    def write_card(self, size=8, is_double=False):
        nodes = self.node_ids
        nodes2 = ['' if node is None else '%8i' % node for node in nodes[4:]]

        data = [self.eid, self.Pid()] + nodes[:4] + nodes2
        msg = ('CTETRA  %8i%8i%8i%8i%8i%8i%8s%8s\n'
               '        %8s%8s%8s%8s' % tuple(data))
        return self.comment() + msg.rstrip() + '\n'

    def __init__(self, card=None, data=None, comment=''):
        SolidElement.__init__(self, card, data)
        if comment:
            self._comment = comment
        if card:
            #: Element ID
            self.eid = integer(card, 1, 'eid')
            #: Property ID
            self.pid = integer(card, 2, 'pid')
            nids = [integer(card, 3, 'nid1'),
                    integer(card, 4, 'nid2'),
                    integer(card, 5, 'nid3'),
                    integer(card, 6, 'nid4'),
                    integer_or_blank(card, 7, 'nid5'),
                    integer_or_blank(card, 8, 'nid6'),
                    integer_or_blank(card, 9, 'nid7'),
                    integer_or_blank(card, 10, 'nid8'),
                    integer_or_blank(card, 11, 'nid9'),
                    integer_or_blank(card, 12, 'nid10'), ]
            assert len(card) <= 13, 'len(CTETRA10 card) = %i' % len(card)
        else:
            self.eid = data[0]
            self.pid = data[1]
            nids = [d if d > 0 else None for d in data[2:]]
            assert len(data) == 12, 'len(data)=%s data=%s' % (len(data), data)
        self.prepare_node_ids(nids, allow_empty_nodes=True)
        assert len(self.nodes) <= 10

    def cross_reference(self, model):
        msg = ' which is required by %s eid=%s' % (self.type, self.eid)
        self.nodes = model.Nodes(self.nodes, allowEmptyNodes=True, msg=msg)
        self.pid = model.Property(self.pid, msg=msg)

    def _verify(self, xref=False):
        eid = self.Eid()
        pid = self.Pid()
        nids = self.node_ids
        assert isinstance(eid, int)
        assert isinstance(pid, int)
        for i, nid in enumerate(nids):
            assert nid is None or isinstance(nid, int), 'nid%i is not an integer/blank; nid=%s' %(i, nid)
        if xref:
            c = self.Centroid()
            v = self.Volume()
            assert isinstance(v, float)
            for i in range(3):
                assert isinstance(c[i], float)

    def N_10(self, g1, g2, g3, g4):
        N1 = g1 * (2 * g1 - 1)
        N2 = g2 * (2 * g2 - 1)
        N3 = g3 * (2 * g3 - 1)
        N4 = g4 * (2 * g4 - 1)
        N5 = 4 * g1 * g2
        N6 = 4 * g2 * g3
        N7 = 4 * g3 * g1
        N8 = 4 * g1 * g4
        N9 = 4 * g2 * g4
        N10 = 4 * g3 * g4
        return (N1, N2, N3, N4, N5, N6, N7, N8, N9, N10)

    def Volume(self):
        """
        Gets the volume, :math:`V`, of the primary tetrahedron.

        .. seealso:: CTETRA4.Volume
        """
        (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10) = self.nodePositions()
        return volume4(n1, n2, n3, n4)

    def Centroid(self):
        """
        Gets the cenroid of the primary tetrahedron.

        .. seealso:: CTETRA4.Centroid
        """
        (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10) = self.nodePositions()
        return (n1 + n2 + n3 + n4) / 4.

    def getFaceNodes(self, nidOpposite, nid=None):
        nids = self.node_ids[:4]
        indx = nids.index(nidOpposite)
        nids.pop(indx)
        return nids

    def nodeIDs(self):
        return self.node_ids

    @property
    def node_ids(self):
        return self._nodeIDs(allowEmptyNodes=True)

    @node_ids.setter
    def node_ids(self, value):
        raise ValueError("You cannot set node IDs like this...modify the node objects")
