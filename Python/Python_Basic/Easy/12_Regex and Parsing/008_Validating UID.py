"008 - Validating UID"

"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
Input format

The first line contains an integer T, the number of test cases. The next T lines contains an employee's UID.

Output format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input 0

2
B1CD102354
B1CDEF2354  
Sample Output 0

Invalid
Valid
"""
import re

for _ in range(int(input())):
    uid = input()

    # It must contain at least 2 uppercase English alphabet characters.
    c1 = len(re.findall(r"[A-Z]", uid)) >= 2

    # It must contain at least 3 digits (0-9).
    c2 = len(re.findall(r"[0-9]", uid)) >= 3  # Corrected here

    # It should only contain alphanumeric characters (a-z, A-Z & 0-9).
    c3 = len(re.findall(r"[a-zA-Z0-9]", uid)) == len(uid)

    # No character should repeat.
    c4 = len(set(uid)) == len(uid)

    # There must be exactly 10 characters in a valid UID.
    c5 = len(uid) == 10

    # Must satisfy all conditions
    print('Valid' if all([c1, c2, c3, c4, c5]) else 'Invalid')
