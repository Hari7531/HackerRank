"008 - Array Mathematics"
"""
Problem

Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.

Task

You are given two integer arrays, A and B of dimensions N X M. Your task is to perform the following operations:

Add (A + B) Subtract (A - B) Multiply (A * B) Integer Division (A / B) Mod (A % B) Power (A ** B)

Input Format

The first line contains two space separated integers, N and M. The next N lines contains M space separated integers of array A. The following N lines contains M space separated integers of array B.

Output Format

Print the result of each operation in the given order under Task.

Sample Input 0

1 4
1 2 3 4
5 6 7 8
Sample Output 0

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

n, m = map(int, input().split())

a = numpy.array([list(map(int, input().split())) for _ in range(n)])
b = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
