#!/usr/bin/env python

from util_sort import swap

# Ascending order algorithm
def insertion_sort(list_test) :
	for x in range(0, len(list_test)):
		y = x
		while y > 0 and list_test[y - 1] > list_test[y]:
			swap(list_test, y, y - 1)
			y = y - 1
	return list_test