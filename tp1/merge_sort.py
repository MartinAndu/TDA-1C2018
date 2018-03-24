#!/usr/bin/env python

def merge_sort(list_test) :
    merge_sort_method(list_test,0 , len(list_test) - 1)
    return list_test

def merge_sort_method(list_test, start, end) :
    if start < end :
        middle = int(( start + end) / 2)
        merge_sort_method(list_test, start, middle)
        merge_sort_method(list_test, middle + 1, end)
        merge(list_test, start, middle , end)


def merge(list_test, start, middle, end) :

    number1 = middle - start + 1
    number2 = end  - middle 

    list_test_left = [None] * (number1 + 1)
    list_test_right = [None] * (number2 + 1)

    for x in range(0, number1) :
        list_test_left[x] = list_test[ start + x ]

    for y in range(0, number2):
        list_test_right[y] = list_test[ middle + y + 1]

    list_test_left[number1] = float('inf')
    list_test_right[number2] = float('inf')
    
    i = 0
    j = 0

    for k in range(start, end + 1)	:
        if list_test_left[i] <= list_test_right[j]:
            list_test[k] = list_test_left[i]
            i = i + 1
        else :
            list_test[k] = list_test_right[j]
            j = j + 1
