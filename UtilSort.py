#!/usr/bin/python

def printList(list) :
	for elem in list:
		print(elem,' ')
	print()


def swap(list, A, B) :
	C = list[A]
	list[A] = list[B]
	list[B] = C