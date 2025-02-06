"001 - Detect Floating Point Number"

"""
Problem
You are given a string N. Your task is to verify that N is a floating point number.

Input Format

The first line contains an integer T, the number of test cases. The next T line(s) contains a string N.

Output Format

Output True or False for each test case.

Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff
Sample Output 0

False
True
True
False

"""



import re

pattern = r'^[\+-]{,1}\d*\.\d+$'

for _ in range(int(input())):
    
    print(True if re.search(pattern, input()) else False)