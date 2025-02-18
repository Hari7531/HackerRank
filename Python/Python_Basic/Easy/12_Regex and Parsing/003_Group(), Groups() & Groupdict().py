"003 - Group(), Groups() & Groupdict()"

"""
Problem
group()
A group() expression returns one or more subgroups of the match.

groups()
A groups() expression returns a tuple containing all the subgroups of the match.

groupdict()
A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.

Task

You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.

Input format

A single line of input containing the string S.

Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

Sample Input 0

..12345678910111213141516171820212223
Sample Output 0

1

"""

import re

m = re.search(r"(?P<repeat>([a-z0-9])\2?(?:\2))+", input())

print(m.groupdict()['repeat'][0] if m else '-1')
