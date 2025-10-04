# "001 - Arrays"

"""
Problem

The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.

Task

You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

Input Format

A single line of input containing space separated numbers.

Output Format

Print the reverse NumPy array with type float.

Sample Input 0

1 2 3 4 -8 -10
Sample Output 0

[-10.  -8.   4.   3.   2.   1.]

"""



import numpy

def arrays(arr):
    return numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Method-2

arr = numpy.array(input().split(), float)   # convert to float
print(arr[::-1])                         # reverse array