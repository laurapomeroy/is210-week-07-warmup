#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple for-loop to loop over a simple data contruct"""


import decimal


def lexicographics(to_analyze):
    """Provides the maximum, minimum, and average length of words

    Args:
        to_analyze(str): analyzes the speech

    Examples:
    >>> lexicographics('Don\'t stop believing, Hold on to that feeling.')
    (8, 8, Decimal('8'))

    """
    lines = to_analyze.split('\n')
    list1 = []
    for line in lines:
        list1.append(len(line.split()))
    return (max(list1), min(list1), sum(list1) / decimal.Decimal(len(list1)))
