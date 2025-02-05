"003 - Any or All"

"""
Problem
This expression returns True if any element of the iterable is true. If the iterable is empty, it will return False.

Task

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format

The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of N integers.

Sample Input 0

5
12 9 61 5 14 
Sample Output 0

True
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def palindromic(n):
    nlist = list(str(n))
    return str.join('', nlist) == str.join('', reversed(nlist))

input()
numbers = list(map(int, input().split()))

is_palindromic = [palindromic(x) for x in numbers]
is_positive = [x >= 0 for x in numbers]

print(all(is_positive) and any(is_palindromic))