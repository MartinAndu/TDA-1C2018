#!/usr/bin/python

from UtilSort import swap

# Ascending order algorithm
def insertionSort(list) :
	for x in range(0, len(list)):
		y = x
		while y > 0 and list[y - 1] > list[y]:
			swap(list, y, y - 1)
			y = y - 1