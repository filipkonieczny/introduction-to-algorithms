#!/usr/bin/env python
# encoding: utf-8


# Introduction to Algorithms
# Chapter 1 - Insertion Sort


# declare variables
case1 = [5, 2, 4, 6, 1, 3]
case2 = [31, 41, 59, 26, 41, 58]
case3 = [123, 321, 132, 343, 231, 111]

cases = [case1, case2, case3]


# main code
def insertion_sort(array_to_sort):
    '''
    Takes an array of numbers and sorts it from lowest to highest.

    (array) -> array


    >>> insertion_sort([5, 2, 4, 6, 1, 3])
    [1, 2, 3, 4, 5, 6]

    '''


    # declare variables
    A = []
    A.extend(array_to_sort)

    N = len(A)


    # corner case - if len(A) is too small
    if N <= 1:
        return A


    # general algorithm working for N > 1
    # for every element starting at position 1
    for i in xrange(1, N):
        # for every element behind current position
        for j in xrange(0, i):
            # check if there are smaller numbers
            if A[i] < A[j]:
                moving_number = A[i]

                # if there are smaller objects, rearrange our array
                for k in reversed(xrange(j, i + 1)):
                    A[k] = A[k - 1]

                A[j] = moving_number


    # return the result
    return A


# printing the results
print("\n\nThese are the results:")

for i, case in enumerate(cases):
    print "#" + str(i + 1), case, "\tinto\t", insertion_sort(case)
    print("\n")