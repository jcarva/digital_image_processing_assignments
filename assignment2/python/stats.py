from random import randrange
import sort
import numpy as np


def median(array):
    if type(array).__module__ == np.__name__:
        array = array.flatten()

    length = len(array)
    sort.sort(array)

    # Odd
    if length % 2 == 1:
        position = length / 2
        return array[position]

    # Even
    else:
        position = len(array) / 2
        return array[position-1] + array[position] / 2.0


def quick_median(array):
    if type(array).__module__ == np.__name__:
        array = array.flatten()

    length = len(array)

    # Odd
    if length % 2 == 1:
        position = length / 2
        return _find_nth(array, position)

    # Even
    else:
        position = len(array) / 2
        return (_find_nth(array, position - 1) + _find_nth(array, position)) / 2.0


def _partition(array, pivot_index=0):
    i = 0
    if pivot_index != 0: array[0], array[pivot_index] = array[pivot_index], array[0]

    for j in range(len(array) - 1):
        if array[j + 1] < array[0]:
            array[j + 1], array[i + 1] = array[i + 1], array[j + 1]
            i += 1

    array[0], array[i] = array[i], array[0]
    return array, i


# https://pythonandr.com/2016/07/18/randomized-selection-algorithm-quickselect-python-code/
def _find_nth(array, position):
    if len(array) == 1:
        return array[0]

    xpart = _partition(array, randrange(len(array)))
    array = xpart[0]  # partitioned array
    j = xpart[1]  # pivot index
    if j == position:
        return array[j]
    elif j > position:
        return _find_nth(array[:j], position)
    else:
        position = position - j - 1
        return _find_nth(array[(j + 1):], position)