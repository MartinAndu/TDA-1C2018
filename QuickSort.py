#!/usr/bin/python

from UtilSort import swap


def quickSort(list) :
	quickSortMethod(list, 0, len(list))
	
# Ascending order algorithm
def quickSortMethod(list, start, end) :
	if ( start < end ):
		newIndex = partition(list, 0, end)
		quickSortMethod(list, start, newIndex - 1)
		quickSortMethod(list, newIndex + 1, end)

def partition(list, start, end) :
	pivot = list[end]
	x = start - 1
	for y in range(start, end - 1):
		if list[y] <= pivot:
			x = x + 1
			swap(list, x, y)
	swap(list, x + 1, end)
	return x + 1