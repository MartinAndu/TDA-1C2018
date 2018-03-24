#!/usr/bin/python

from selection_sort import selection_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from merge_sort import merge_sort


import random

'''
for i in range(10) :
	l = list(range(10))
	random.shuffle(l)
	ordenada = sorted(l)
	print ("Original\n", l, "\n")
	mergeSort(l)
	print ("Sorted\n", l, "\n")
'''

l = list(range(0, 20))
random.shuffle(l)

print ("Original\n", l, "\n")
quick_sort(l)
print ("Sorted\n", l, "\n")

