"013 - Inner and Outer"
"""
Problem

inner The inner tool returns the inner product of two arrays.

outer The outer tool returns the outer product of two arrays.

Task

You are given two arrays: A and B.
Your task is to compute their inner and outer product.

Input Format

The first line contains the space separated elements of array A. The second line contains the space separated elements of array B.

Output Format

First, print the inner product. Second, print the outer product.

Sample Input 0

0 1
2 3
Sample Output 0

3
[[0 0]
 [2 3]]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(np.inner(a, b))
print(np.outer(a, b))
