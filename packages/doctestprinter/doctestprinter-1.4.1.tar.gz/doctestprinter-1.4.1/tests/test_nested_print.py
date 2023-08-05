from abc import ABC, abstractmethod
from typing import Any, Callable, List, Tuple, Union, Mapping, Sequence, Optional

import pandas
import treenodedefinition

from doctestprinter import (
    prepare_pandas,
    prepare_print,
    default_value_conversion,
    _nested_data_to_print_table,
    RightAlignedLeafKeys,
)
from pandas import DataFrame
import numpy as np
from pandas import DataFrame

sample_frame_1 = DataFrame(
    np.arange(12).reshape(4, 3),
    index=["1st", "2nd", "3rd", "4rd"],
    columns=["A", "B", "C"],
)
sample_frame_2 = DataFrame(
    np.arange(8).reshape(2, 4),
    index=["1st", "2nd"],
    columns=[
        "A_really_very",
        "wide_table",
        "which_exceeds_the",
        "remaining_column_width.",
    ],
)

_lorem_ipsum = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Vivamus ut vulputate turpis, sed vehicula eros. Donec ac"
    " mollis elit. Aliquam luctus tortor at lacinia auctor."
    " Donec convallis, sapien et vulputate consequat, sapien"
    " odio dignissim arcu, in auctor nisl lectus malesuada"
    " tortor."
)

nested_sample_1 = {
    "1st_level_1st_item": {"2nd_level_1st_item": "A short entry."},
    "1st_level_2nd_item": (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Vivamus ut vulputate turpis, sed vehicula eros. Donec ac mollis elit. "
        "Aliquam luctus tortor at lacinia auctor. Donec convallis, sapien et "
    ),
    "1st_level_3rd_item": {
        "2nd_level_1st_item": sample_frame_1,
        "2nd_level_2nd_item": sample_frame_2,
    },
}


def test_default_item_conversion_sample_1():
    """
    >>> print(test_default_item_conversion_sample_1())
    Lorem ipsum dolor sit amet, consectetur adipiscing
    elit. Vivamus ut vulputate turpis, sed vehicula eros.
    Donec ac mollis elit. Aliquam luctus tortor at lacinia
    auctor. Donec convallis, sapien et vulputate consequat,
    sapien odio dignissim arcu, in auctor nisl lectus malesuada
    tortor.
    """
    return default_value_conversion(_lorem_ipsum, remaining_column_width=50)


def test_nested_to_raw_table_sample_1():
    """
    Test if the table contains the objects instead of string representations.
    """
    print_table = _nested_data_to_print_table(
        nested_sample_1, treenodedefinition.this_item_is_a_leaf
    )
    assert isinstance(print_table["row_value"][5], DataFrame)


def test_print_tree_sample_1():
    """
    Test various outcomes.

    >>> from doctestprinter import print_tree
    >>> print_tree(nested_sample_1, max_column_width=70)
    {.
    # 1st_level_1st_item  {.
        2nd_level_1st_item : A short entry.
        1st_level_2nd_item : Lorem ipsum dolor sit amet, consectetur adipiscing
                             elit. Vivamus ut vulputate turpis, sed vehicula eros.
                             Donec ac mollis elit. Aliquam luctus tortor at lacinia
                             auctor. Donec convallis, sapien et
    # 1st_level_3rd_item  {.
        2nd_level_1st_item :      A   B   C
                             1st  0   1   2
                             2nd  3   4   5
                             3rd  6   7   8
                             4rd  9  10  11
        2nd_level_2nd_item :
               A_really_very  wide_table  which_exceeds_..  remaining_colu..
          1st              0           1                 2                 3
          2nd              4           5                 6                 7

    """


def test_RightAlignedLeafKeys_make_value_column_repr_sample_1():
    """
    Test generating the values.

    >>> from doctestprinter import doctest_iter_print
    >>> value_samples = test_RightAlignedLeafKeys_make_value_column_repr_sample_1()
    >>> doctest_iter_print(value_samples)
    <BLANKLINE>
    <BLANKLINE>
    A short entry.
    Lorem ipsum dolor sit amet, consectetur adipiscing
                             elit. Vivamus ut vulputate turpis, sed vehicula eros.
                             Donec ac mollis elit. Aliquam luctus tortor at lacinia
                             auctor. Donec convallis, sapien et
    <BLANKLINE>
         A   B   C
                             1st  0   1   2
                             2nd  3   4   5
                             3rd  6   7   8
                             4rd  9  10  11
    <BLANKLINE>
               A_really_very  wide_table  which_exceeds_..  remaining_colu..
          1st              0           1                 2                 3
          2nd              4           5                 6                 7

    """
    sample_formatter = RightAlignedLeafKeys()
    print_table = _nested_data_to_print_table(
        nested_sample_1, treenodedefinition.this_item_is_a_leaf
    )
    sample_formatter._make_key_column_repr(print_table=print_table)
    sample_formatter._make_value_column_repr(print_table=print_table)
    col_name = RightAlignedLeafKeys.ColumnNames.VALUE_REPRESENTATION
    return print_table[col_name]
