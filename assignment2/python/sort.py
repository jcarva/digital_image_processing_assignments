# Author: Jaelson Carvalho
# Python 3,4
# Usage: python3.4 quick.py

import random


def sort(sample):
    "This QuickSort function just is a interface to maintain the pattern to pass only a sample as argument."

    "Call the quicksort logic"
    quicksort(sample, 0, len(sample)-1)

    return sample


def quicksort(sample, init, final):
    "Set left index"
    i = init

    "Set right index"
    j = final

    "Select pivot value"
    pivot = random.choice(sample[init:final])

    while i < j:
        "Search a higher value than the pivot in left side"
        while sample[i] < pivot:
            i += 1

        "Search a lower value than the pivot in left side"
        while sample[j] > pivot:
            j -= 1

        "Switch a lower value to a higher value, when we have the as reference"
        if i <= j:
            aux = sample[i]
            sample[i] = sample[j]
            sample[j] = aux
            i += 1
            j -= 1

    "Call the recursion to left side"
    if j > init:
        quicksort(sample, init, j)

    "Call the recursion to right side"
    if i < final:
        quicksort(sample, i, final)