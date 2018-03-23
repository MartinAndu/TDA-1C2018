#!/usr/bin/python

from UtilSort import swap

# Ascending order algorithm
def heapSort(list) :
	heapSize = len(list) - 1
	buildHeap(list, heapSize)
	for x in range(len(list) - 1, 0, -1) :
		swap(list, 0, x)
		heapSize = heapSize - 1
		maxHeapify(list, heapSize, 0)


def buildHeap(list, heapSize) :
	for x in range(int((len(list) - 1) / 2), -1, -1) :
		maxHeapify(list, heapSize, x)

def maxHeapify(list, heapSize, index):
 l = left(index)
 r = right(index)

 if l <= heapSize and list[l] > list[index] :
  largest = l
 else : 
  largest = index

 if r <= heapSize and list[r] > list[largest] :
  largest = r

 if largest != index :
  swap(list, index, largest)
  maxHeapify(list, heapSize, largest)


def left(index):
	return index * 2

def right(index):
	return index * 2 + 1