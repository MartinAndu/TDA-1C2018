#!/usr/bin/env python

from util_sort import swap

# Ascending order algorithm
def selection_sort(list_test) :
	for x in range(0, len(list_test) - 1):
		for y in range(x, len(list_test)):
			if list_test[x] > list_test[y]:
				swap(list_test, x, y)
	return list_test