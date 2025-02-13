"007 - Mean, Var, and Std"

"""
Problem

mean The mean tool computes the arithmetic mean along the specified axis.
By default, the axis is None. Therefore, it computes the mean of the flattened array.

var The var tool computes the arithmetic variance along the specified axis.
By default, the axis is None. Therefore, it computes the variance of the flattened array.

std The std tool computes the arithmetic standard deviation along the specified axis.
By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.

Task

You are given a 2-D array of size N X M. Your task is to find:

The mean along axis 1
The var along axis 0
The std along axis None
Input Format

The first line of input contains space separated values of N and M. The next N lines contains M space separated integers.

Output Format

First, print the mean. Second, print the var. Third, print the std.

Sample Input 0

2 2
1 2
3 4
Sample Output 0

[ 1.5  3.5]
[ 1.  1.]
1.11803398875
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N,M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(A.mean(axis=1))
print(A.var(axis=0))
print(numpy.round(A.std(), decimals=11))