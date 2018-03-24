#!/usr/bin/env python

from util_sort import swap

# Ascending order algorithm
def heap_sort(list_test) :
  heap_size = len(list_test) - 1
  build_heap(list_test, heap_size)
  for x in range(len(list_test) - 1, 0, -1) :
    swap(list_test, 0, x)
    heap_size = heap_size - 1
    max_heapify(list_test, heap_size, 0)


def build_heap(list_test, heap_size) :
 for x in range(int((len(list_test) - 1) / 2), -1, -1) :
  max_heapify(list_test, heap_size, x)

def max_heapify(list_test, heap_size, index):
 l = left(index)
 r = right(index)

 if l <= heap_size and list_test[l] > list_test[index] :
  largest = l
 else : 
  largest = index

 if r <= heap_size and list_test[r] > list_test[largest] :
  largest = r

 if largest != index :
  swap(list_test, index, largest)
  max_heapify(list_test, heap_size, largest)


def left(index):
	return index * 2

def right(index):
	return index * 2 + 1