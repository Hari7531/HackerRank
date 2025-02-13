"010 - Sum and Prod"
"""
Problem

sum The sum tool returns the sum of array elements over a given axis.
By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

prod The prod tool returns the product of array elements over a given axis. By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.

Task

You are given a 2-D array with dimensions N X M. Your task is to perform the sum tool over axis 0 and then find the product of that result.

Input Format

The first line of input contains space separated values of N and M. The next N lines contains M space separated integers.

Output Format

Compute the sum along axis 0. Then, print the product of that sum.

Sample Input 0

2 2
1 2
3 4
Sample Output 0

24
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

print(np.prod(np.sum(np.array(arr), axis = 0)))
