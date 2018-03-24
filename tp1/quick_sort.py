#!/usr/bin/env python

from util_sort import swap

def quick_sort(list_test) :
	quick_sort_method(list_test, 0, len(list_test) - 1)
	return list_test
	
# Ascending order algorithm
def quick_sort_method(list_test, start, end) :
	if ( start < end ):
		newIndex = partition(list_test, start, end)
		quick_sort_method(list_test, start, newIndex - 1)
		quick_sort_method(list_test, newIndex + 1, end)

def partition(list_test, start, end) :
	pivot = list_test[end]
	x = start - 1
	for y in range(start, end):
		if list_test[y] <= pivot:
			x = x + 1
			swap(list_test, x, y)
	swap(list_test, x + 1, end)
	return x + 1