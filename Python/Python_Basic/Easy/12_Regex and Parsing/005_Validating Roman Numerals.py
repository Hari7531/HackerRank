"005 - Validating Roman Numerals"

"""
Problem
You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

Input format

A single line of input containing a string of Roman characters.

Output format

Output a single line containing True or False according to the instructions above.

Sample Input 0

CDXXI
Sample Output 0

True

"""
m = "M{,3}(CM){,1}"
d = "(D{,1}|CD)"
c = "C{,3}(XC){,1}"
l = "(L{,1}|XL)"
x = "X{,3}(IX){,1}"
i = "(V{,1}I{,3}|IV)"

regex_pattern = r"^%s%s%s%s%s%s$" % (m, d, c, l, x, i)

import re
print(str(bool(re.match(regex_pattern, input()))))
