#!/usr/bin/env python
# encoding: utf-8


# Introduction to Algorithms
# Chapter 1 - Binary Adding(1.1.4)


# declare variables
case1 = ([1, 0, 0, 1], [1, 1, 0, 1])
case2 = ([1, 1, 0, 1, 0, 1], [1, 0, 1])
case3 = ([1, 0], [1, 1, 1, 1, 1])

cases = [case1, case2, case3]


# main code
def insertion_sort(A, B):
    '''
    Takes 2 binary numbers, adds them, returns the sum.

    (array, array) -> array


    >>> insertion_sort(1001, 1101)
    10110

    '''


    # declare variables
    N_A = len(A)
    N_B = len(B)

    A = A[::-1]
    B = B[::-1]


    # figure out which array is longer
    if N_A >= N_B:
        N = N_A + 1

    else:
        N = N_B + 1

    result = [0] * N


    # perform adding
    for i in xrange(N_A):
        result[i] += A[i]

    for i in xrange(N_B):
        result[i] += B[i]


    # reduce any 2s
    for i in xrange(N):
        if result[i] == 2:
            result[i] = 0
            result[i + 1] += 1


    result = result[::-1]


    # return the result
    if result[0] == 0:
        return result[1:]

    else:
        return result
    


# printing the results
print("\n\nThese are the results:")

for i, case in enumerate(cases):
    print "#" + str(i + 1), case, "\t->\t", insertion_sort(case[0], case[1])
    print("\n")