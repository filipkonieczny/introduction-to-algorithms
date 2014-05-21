#!/usr/bin/env python
# encoding: utf-8


# Introduction to Algorithms
# Chapter 1 - Linear Search(1.1.3)


# declare variables
case1 = ([5, 2, 4, 6, 1, 3], 1)
case2 = ([31, 41, 59, 26, 41, 58], 0)
case3 = ([123, 321, 132, 343, 231, 111], 111)

cases = [case1, case2, case3]


# main code
def insertion_sort(array_to_sort, V):
    '''
    Takes an array of numbers and searches for a number that's equal to V.
    Returns the index of a found match.
    Returns -1 if no matches are found.

    (array, int) -> int


    >>> insertion_sort([5, 2, 4, 6, 1, 3], 1)
    4

    >>> insertion_sort([5, 2, 4, 6, 1, 3], 0)
    -1

    '''


    # declare variables
    A = []
    A.extend(array_to_sort)

    N = len(A)


    # search for the equivalent of V
    for i, number in enumerate(A):
        if number == V:
            return i

    # if no equivalents were found
    return -1
    


# printing the results
print("\n\nThese are the results:")

for i, case in enumerate(cases):
    print "#" + str(i + 1), case, "\t->\t", insertion_sort(case[0], case[1])
    print("\n")