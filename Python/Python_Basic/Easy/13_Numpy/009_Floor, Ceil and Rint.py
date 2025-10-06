"009 - Floor, Ceil and Rint"

"""
Problem

floor The tool floor returns the floor of the input element-wise. The floor of x is the largest integer i where i <= x.

ceil The tool ceil returns the ceiling of the input element-wise. The ceiling of x is the smallest integer i where i >= x.

rint The rint tool rounds to the nearest integer of input element-wise.

Task

You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.

Input Format

A single line of input containing the space separated elements of array A.

Output Format

On the first line, print the floor of A. On the second line, print the ceil of A. On the third line, print the rint of A.

Sample Input 0

1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
Sample Output 0

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

a = list(map(float, input().split()))

# to fix the ouput format,Always reserve a space for positive numbers instead of showing a + or nothing
np.set_printoptions(sign=' ')

print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))