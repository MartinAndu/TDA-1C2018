#!/usr/bin/env python

from util_sort import swap

# Ascending order algorithm
def selection_sort(list_test) :
    for x in range(len(list_test) - 1, 1, -1):
        pos_of_max = 0
        for y in range(x, len(list_test)):
            if list_test[y] > list_test[pos_of_max]:
                pos_of_max = y
        swap(list_test, x, pos_of_max)
    return list_test
