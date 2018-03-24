#!/usr/bin/python

from UtilSort import swap

# Ascending order algorithm
def selectionSort(list) :
	for x in range(0, len(list) - 1):
		for y in range(x, len(list)):
			if list[x] > list[y]:
				swap(list, x, y)