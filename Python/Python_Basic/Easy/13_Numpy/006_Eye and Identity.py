"006 - Eye and Identity"

"""
Problem

identity The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0. The default type of elements is float.

eye The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter k. A positive k is for the upper diagonal, a negative is for the lower, and a 0 k (default) is for the main diagonal.

Task

Your task is to print an array of size N X M with its main diagonal elements as 1's and 0's everywhere else.

Input Format

A single line containing the space separated values of N and M. N denotes the rows. M denotes the columns.

Output Format

Print the desired N X M array.

Sample Input 0

3 3
Sample Output 0

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
"""
# Method-1
import numpy

n, m = map(int, input().split())

# to fix the ouput format
numpy.set_printoptions(sign=' ')

print(numpy.eye(n, m))

# Method-2

# Take input
n, m = map(int, input().split())

# Create the array
print(numpy.eye(n, m))
