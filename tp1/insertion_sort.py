#!/usr/bin/env python

from util_sort import swap

# Ascending order algorithm
def insertion_sort(list_test) :
    for y in range(1, len(list_test)) :
        key = list_test[y]
        x = y - 1
        while x > 0 and list_test[x] > key :
            list_test[x + 1] = list_test[x]
            x = x - 1
        list_test[x + 1] = key
    return list_test
