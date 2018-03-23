#!/usr/bin/python

import sys




def mergeSort(list) :
 mergesortMethod(list,0 , len(list) - 1)

def mergesortMethod(list, start, end) :
 if start < end :
 	middle = int(( start + end) / 2)
 	mergesortMethod(list, start, middle)
 	mergesortMethod(list, middle + 1, end)
 	merge(list, start, middle , end)


def merge(list, start, middle, end) :

	number1 = middle - start + 1
	number2 = end - middle 

	listLeft = [None] * (number1 + 1)
	listRight = [None] * (number2 + 1)


	for x in range(0, number1) :
	 listLeft[x] = list[ start + x - 1]

	for y in range(0, number2):
	 listRight[y] = list[ middle + y]

	listLeft[number1] = sys.maxsize
	listRight[number2] = sys.maxsize
	x = 0
	y = 0

	for z in range(start, end )	:
	 if listLeft[x] <= listRight[y]:
	  list[z] = listLeft[x]
	  x = x + 1
	 else :
	  list[z] = listRight[y]
	  y = y + 1


