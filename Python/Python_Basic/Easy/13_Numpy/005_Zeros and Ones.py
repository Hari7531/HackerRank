"005 - Zeros and Ones"

"""
Problem

zeros The zeros tool returns a new array with a given shape and type filled with 0's.

ones The ones tool returns a new array with a given shape and type filled with 1's.

Task

You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format

A single line containing the space-separated integers.

Output Format

First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

Sample Input 0

3 3 3
Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
"""
import numpy

shape = list(map(int, input().split()))

print(numpy.zeros(shape, dtype = numpy.int))
print(numpy.ones(shape, dtype = numpy.int))
