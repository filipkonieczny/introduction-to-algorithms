#!/usr/bin/env python
# encoding: utf-8


# Introduction to Algorithms
# Chapter 1 - Selection Sort(1.2.1)


# declare variables
case1 = [5, 2, 4, 6, 1, 3]
case2 = [31, 41, 59, 26, 41, 58]
case3 = [123, 321, 132, 343, 231, 111]

cases = [case1, case2, case3]


# main code
def selection_sort(array_to_sort):
    '''
    Takes an array of numbers and sorts it from lowest to highest.
    The procedure is to go through each element of an array.
    Find the lowest, place it on position 1, etc.

    (array) -> array


    >>> selection_sort([5, 2, 4, 6, 1, 3])
    [1, 2, 3, 4, 5, 6]

    '''


    # declare variables
    A = []
    A.extend(array_to_sort)

    B = [0] * len(A)

    current_lowest = A[0]
    lowest_number_position = 0
    current_position = 0


    # execute this algorithm until there are no elements left
    while len(A) > 1:
        # for every number that's in the array
        for i, number in enumerate(A):
            # check if it's currently the lowest
            if number <= current_lowest:
                current_lowest = number
                lowest_number_position = i

        # assign the current lowest number
        B[current_position] = current_lowest
        current_position += 1

        # remove the lowest number from the array, reset values
        A.pop(lowest_number_position)
        current_lowest = A[0]
        lowest_number_position = 0


    B[-1] = A[0]


    # return the result
    return B


# printing the results
print("\n\nThese are the results:")

for i, case in enumerate(cases):
    print "#" + str(i + 1), case, "\tinto\t", selection_sort(case)
    print("\n")