#!/usr/bin/python

from SelectionSort import selectionSort
from InsertionSort import insertionSort
from QuickSort import quickSort
from HeapSort import heapSort
from MergeSort import mergeSort


import random

for i in range(10) :
	l = list(range(10))
	random.shuffle(l)
	ordenada = sorted(l)
	print ("Original\n", l, "\n")
	mergeSort(l)
	print ("Sorted\n", l, "\n")
