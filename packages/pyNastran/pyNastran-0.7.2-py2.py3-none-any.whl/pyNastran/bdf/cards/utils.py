from six import string_types

def build_table_lines(fields, nstart=1, nend=0):
    """
    Builds a table of the form:

    +--------+-------+--------+-------+--------+-------+-------+-------+
    | DESVAR | DVID1 | DVID2  | DVID3 |DVID4   | DVID5 | DVID6 | DVID7 |
    +--------+-------+--------+-------+--------+-------+-------+-------+
    |        | DVID8 | -etc.- |       |        |       |       |       |
    +--------+-------+--------+-------+--------+-------+-------+-------+
    |        |  UM   | VAL1   | VAL2  | -etc.- |       |       |       |
    +--------+-------+--------+-------+--------+-------+-------+-------+

    and then pads the rest of the fields with None's

    :param fields: the fields to enter, including DESVAR
    :type fields:  list of values
    :param nStart: the number of blank fields at the start of the
                   line (default=1)
    :param nStart: int
    :param nEnd:   the number of blank fields at the end of the
                   line (default=0)
    :param nEnd:   int

    .. note:: will be used for DVPREL2, RBE1, RBE3
    .. warning:: only works for small field format???
    """
    fields_out = []
    n = 8 - nstart - nend

    # pack all the fields into a list.  Only consider an entry as isolated
    for (i, field) in enumerate(fields):
        fields_out.append(field)
        if i > 0 and i % n == 0:  # beginning of line
            #pad = [None] * (i + j)
            #fields_out += pad
            fields_out += [None] * (nstart + nend)

    # make sure they're aren't any trailing None's (from a new line)
    fields_out = wipe_empty_fields(fields_out)

    # push the next key (aka next fields[0]) onto the next line
    nspaces = 8 - (len(fields_out)) % 8  # puts UM onto next line
    if nspaces < 8:
        fields_out += [None] * nspaces
    return fields_out


def wipe_empty_fields(card):
    """
    Removes an trailing Nones from the card.
    Also converts empty strings to None.

    :param card:         the fields on the card as a list
    :returns short_card: the card with no trailing blank fields

    .. todo:: run this in reverse to make it faster
    """
    short_card = []
    for field in card:
        if isinstance(field, string_types):
            field = field.strip()
            if field == '':
                field = None
        short_card.append(field)

    i = 0
    imax = 0
    while i < len(card):
        if short_card[i] is not None:
            imax = i
        i += 1
    return short_card[:imax + 1]
