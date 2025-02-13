"012 - Dot and Cross"

"""
Problem

dot The dot tool returns the dot product of two arrays.

cross The cross tool returns the cross product of two arrays.

Task

You are given two arrays A and B. Both have dimensions of N X N.
Your task is to compute their matrix product.

Input Format

The first line contains the integer N.
The next N lines contains N space separated integers of array B.
The following N lines contains N space separated integers of array B.

Output Format

Print the matrix multiplication of A and B.

Sample Input 0

2
1 2
3 4
1 2
3 4
Sample Output 0

[[ 7 10]
 [15 22]]
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

print(np.dot(a, b))
