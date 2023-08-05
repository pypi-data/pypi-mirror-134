from doctestprinter import _RawTreeTableRow, _ContainerIndex, ContainerType


def test_item_breaking_sample_1():
    """
    >>> from doctestprinter import doctest_print
    >>> doctest_print(test_item_breaking_sample_1(), max_line_width=50, show_ruler=True)
    0....,....10...,....20...,....30...,....40...,....50
    _RawTreeTableRow(index=_ContainerIndex(depth=0, position=0,
    container_type=<ContainerType.SEQUENCE: 1>, is_leaf=True),
    row_key=, row_value=)
    """
    return _RawTreeTableRow(_ContainerIndex(0, 0, ContainerType.SEQUENCE, True), "", "")