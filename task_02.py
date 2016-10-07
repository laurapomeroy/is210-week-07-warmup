#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create a small function that can return a 'yes' or 'no' value"""


def bool_to_str(bval):
    """Function that returns a 'yes' or 'no' value

    Args:
        bval(bool): A boolean-like value evaluated for truthiness or falsiness

    Returns
        The string 'Yes' or 'No'

    Examples:
        >>> bool_to_str('')
        'No'
        >>> bool_to_str(1)
        'Yes'

    """
    if bval:
        return 'Yes'
    else:
        return 'No'
