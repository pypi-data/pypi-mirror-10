from numpy import angle
from pyNastran.utils import object_attributes


def writeFloats10E(vals):
    vals2 = []
    isAllZeros = True
    for v in vals:
        v2 = '%10.3E' % v
        if v2 == ' 0.000E+00' or v2 == '-0.000E+00':
            v2 = ' 0.0'
        else:
            isAllZeros = False
        vals2.append(v2)
    return vals2, isAllZeros


def writeFloats12E(vals):
    vals2 = []
    isAllZeros = True
    for v in vals:
        v2 = '%12.5E' % v
        if v2 == ' 0.00000E+00' or v2 == '-0.00000E+00':
            v2 = ' 0.0'
        else:
            isAllZeros = False
        vals2.append(v2)
    return vals2, isAllZeros


def writeFloats13E(vals):
    vals2 = []
    isAllZeros = True
    for v in vals:
        v2 = '%13.6E' % v
        if v2 == ' 0.000000E+00' or v2 == '-0.000000E+00':
            v2 = ' 0.0'
        else:
            isAllZeros = False
        vals2.append(v2)
    return vals2, isAllZeros


def writeImagFloats13E(vals, isMagPhase):
    vals2 = []
    isAllZeros = True

    if isMagPhase:
        for v in vals:
            v2 = '%13.6E' % abs(v)
            if v2 == ' 0.000000E+00' or v2 == '-0.000000E+00':
                v2 = ' 0.0'
            else:
                isAllZeros = False
            vals2.append(v2)

        for v in vals:
            v3 = '%13.6E' % angle(v, deg=True)
            if v3 == ' 0.000000E+00' or v3 == '-0.000000E+00':
                v3 = ' 0.0'
            else:
                isAllZeros = False
            vals2.append(v3)
    else:
        for v in vals:
            v2 = '%13.6E' % v.real
            if v2 == ' 0.000000E+00' or v2 == '-0.000000E+00':
                v2 = ' 0.0'
            else:
                isAllZeros = False
            vals2.append(v2)

        for v in vals:
            v3 = '%13.6E' % v.imag
            if v3 == ' 0.000000E+00' or v3 == '-0.000000E+00':
                v3 = ' 0.0'
            else:
                isAllZeros = False
            vals2.append(v3)
    return vals2, isAllZeros


def writeFloats8p4F(vals):
    vals2 = []
    isAllZeros = True
    for v in vals:
        if v >= 1000.0 or v <= -100.0:
            raise RuntimeError(v)
        v2 = '%8.4f' % v
        if v2 == '  0.0000' or v2 == ' -0.0000':
            v2 = '  0.0   '
        else:
            isAllZeros = False
        vals2.append(v2)
    return vals2, isAllZeros


def _eigenvalue_header(obj, header, itime, ntimes, dt):
    if obj.nonlinear_factor is not None:
        name = obj.data_code['name']
        if isinstance(dt, int):
            dt_line = ' %14s = %i\n' % (name.upper(), dt)
        else:
            dt_line = ' %14s = %12.5E\n' % (name, dt)
        header[1] = dt_line
        codes = getattr(obj, name + 's')
        if not len(codes) == ntimes:
            msg = '%ss in %s the wrong size; ntimes=%s; %ss=%s\n' % (name,
                obj.__class__.__name__, ntimes, name, codes)
            atts = object_attributes(obj)
            msg += 'names=%s\n' % atts
            msg += 'data_names=%s\n' % obj.dataNames
            raise IndexError(msg)

        if hasattr(obj, 'eigr'):
            try:
                eigenvalue_real = obj.eigrs[itime]
            except IndexError:
                msg = 'eigrs[%s] not found; ntimes=%s; eigrs=%s' % (itime, ntimes, obj.eigrs)
                msg += 'names=%s' % object_attributes(obj)
                raise IndexError(msg)
            eigr_line = ' %14s = %12.6E\n' % ('EIGENVALUE', eigenvalue_real)
            header[2] = eigr_line
    return header


def get_key0_compare(adict):
    """Gets the "first" key in a dictionary

    The entry is kind of irrelevant.
    """
    keys = list(adict.keys())
    return keys[0]


def get_key0(adict):
    """Gets the "first" key in a dictionary

    The entry is kind of irrelevant.
    """
    keys = list(adict.keys())
    return keys[0]
