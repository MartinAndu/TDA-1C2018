#!/usr/bin/python

from SelectionSort import selectionSort
from InsertionSort import insertionSort
from QuickSort import quickSort
from HeapSort import heapSort

from UtilSort import printList

list = [26, 54, 93, 17, 77, 31, 44, 55, 20]

printList(list)
heapSort(list)
printList(list)