"014 - Linear Algebra"

"""
Problem

The NumPy module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module linalg.

linalg.det
The linalg.det tool computes the determinant of an array.

linalg.eig
The linalg.eig computes the eigenvalues and right eigenvectors of a square array.

linalg.inv
The linalg.inv tool computes the (multiplicative) inverse of a matrix.

Task

You are given a square matrix A with dimensions N X N.
Your task is to find the determinant.
Note: Round the answer to 2 places after the decimal.

Input Format

The first line contains the integer N.
The next N lines contains the N space separated elements of array A.

Output Format

Print the determinant of A.

Sample Input 0

2
1.1 1.1
1.1 1.1
Sample Output 0

0.0
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

# to fix the ouput format
np.set_printoptions(legacy='1.13')

arr = [list(map(float, input().split())) for _ in range(int(input()))]
    
print(np.linalg.det(arr))
