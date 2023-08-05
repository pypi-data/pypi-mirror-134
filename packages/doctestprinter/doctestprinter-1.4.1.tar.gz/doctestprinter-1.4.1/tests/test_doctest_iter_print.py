_lorem_ipsum = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Vivamus ut vulputate turpis, sed vehicula eros. Donec ac mollis elit. "
    "Aliquam luctus tortor at lacinia auctor. Donec convallis, sapien et "
    "vulputate consequat, sapien odio dignissim arcu, in auctor nisl lectus "
    "malesuada tortor. Etiam iaculis lectus quis massa auctor scelerisque. "
    "Aliquam id lobortis est. Fusce tempor nisl in ultricies luctus. Sed  "
    "vehicula gravida libero. Orci varius natoque penatibus et magnis dis "
    "parturient montes, nascetur ridiculus mus. Vivamus at varius risus. "
    " Nunc ut massa a mi posuere finibus."
)


def test_iter_print_with_max_line_width_with_single_entry():
    """

    >>> from doctestprinter import doctest_iter_print
    >>> max_line_sample = test_iter_print_with_max_line_width_with_single_entry()
    >>> doctest_iter_print(max_line_sample, max_line_width=30)
    Lorem Ipsum:
      Lorem ipsum dolor sit amet, consectetur
      adipiscing elit. Vivamus ut vulputate
      turpis, sed vehicula eros. Donec
      ac mollis elit. Aliquam luctus
      tortor at lacinia auctor. Donec
      convallis, sapien et vulputate
      consequat, sapien odio dignissim
      arcu, in auctor nisl lectus malesuada
      tortor. Etiam iaculis lectus
      quis massa auctor scelerisque.
      Aliquam id lobortis est. Fusce
      tempor nisl in ultricies luctus.
      Sed  vehicula gravida libero.
      Orci varius natoque penatibus
      et magnis dis parturient montes,
      nascetur ridiculus mus. Vivamus
      at varius risus.  Nunc ut massa
      a mi posuere finibus.

    """
    wide_sample = {"Lorem Ipsum": _lorem_ipsum}
    return wide_sample

def test_iter_print_with_max_line_width_with_long_block_entries():
    """

    >>> from doctestprinter import doctest_iter_print
    >>> max_line_sample = test_iter_print_with_max_line_width_with_long_block_entries()
    >>> doctest_iter_print(max_line_sample, max_line_width=30)
    Lorem Ipsum:
      ['Loremipsumdolorsitamet,consecteturadipiscingelit.Vivamusutvulputateturpis,sedvehiculae',
      'Loremipsumdolorsitamet,consecteturadipiscingelit.Vivamusutvulputateturpis,sedvehiculae',
      'Loremipsumdolorsitamet,consecteturadipiscingelit.Vivamusutvulputateturpis,sedvehiculae']


    """
    long_line_item = _lorem_ipsum[:100].replace(" ", "")
    long_test_items = [long_line_item] * 3
    wide_sample = {"Lorem Ipsum": long_test_items}
    return wide_sample


def test_iter_print_with_max_line_width_with_breakable_items():
    """

    >>> from doctestprinter import doctest_iter_print
    >>> max_line_sample = test_iter_print_with_max_line_width_with_breakable_items()
    >>> doctest_iter_print(max_line_sample, max_line_width=30)
    Lorem Ipsum:
      ['Lorem ipsum dolor sit amet,
      consectetur adipiscing elit.
      Vivamus ut vulputate turpis,
      sed vehicula e', 'Lorem ipsum
      dolor sit amet, consectetur adipiscing
      elit. Vivamus ut vulputate turpis,
      sed vehicula e', 'Lorem ipsum
      dolor sit amet, consectetur adipiscing
      elit. Vivamus ut vulputate turpis,
      sed vehicula e']

    """
    long_line_item = _lorem_ipsum[:100]
    long_test_items = [long_line_item] * 3
    wide_sample = {"Lorem Ipsum": long_test_items}
    return wide_sample
