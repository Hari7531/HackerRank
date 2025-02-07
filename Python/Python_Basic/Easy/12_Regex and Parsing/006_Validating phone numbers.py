"006 - Validating phone numbers"

"""
Problem
Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7, 8 or 9.

Input format

The first line contains an integer N, the number of inputs. N lines follow, each containing some string.

Output format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input 0

2
9587456281
1252478965
Sample Output 0

YES
NO

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

regex_pattern = "^[789]{1}[0-9]{9}$"

[print("YES" if re.match(regex_pattern, input()) else "NO") for _ in range(int(input()))]
