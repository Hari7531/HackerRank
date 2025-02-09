"002 - Shape and Reshape"


"""
Problem

The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.

Task

You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

Input Format

A single line of input containing 9 space separated integers.

Output Format

Print the 3X3 NumPy array.

Sample Input 0

1 2 3 4 5 6 7 8 9
Sample Output 0

[[1 2 3]
 [4 5 6]
 [7 8 9]]
 
"""
import numpy

arr = numpy.array(list(map(int, input().split())))
arr.shape = (3, 3)

print(arr)