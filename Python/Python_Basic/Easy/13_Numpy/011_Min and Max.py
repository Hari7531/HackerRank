"011 - Min and Max"

"""
Problem

min The tool min returns the minimum value along a given axis.
By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

max The tool max returns the maximum value along a given axis.
By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.

Task

You are given a 2-D array with dimensions N X M. Your task is to perform the min function over axis 1 and then find the max of that.

Input Format

The first line of input contains space separated values of N and M. The next N lines contains M space separated integers.

Output Format

Compute the min along axis 1 and then print the max of that result.

Sample Input 0

4 2
2 5
3 7
1 3
4 0
Sample Output 0

3

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

print(np.max(np.min(np.array(arr), axis = 1)))
