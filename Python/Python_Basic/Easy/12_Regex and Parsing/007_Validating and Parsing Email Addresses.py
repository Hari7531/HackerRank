"007 - Validating and Parsing Email Addresses"

"""
Problem
A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is 1, 2, or 3 characters in length.
Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

Input Format

The first line contains a single integer, n, denoting the number of email address. Each line i of the n subsequent lines contains a name and an email address as two space-separated values following this

name <user@email.com>
Output Format

Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on a new line in the following format:

name <user@email.com>
You must print each valid email address in the same order as it was received as input.

Sample Input 0

2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
Sample Output 0

DEXTER <dexter@hotmail.com>
"""




import email.utils, re

pattern = '^[a-z][a-z0-9-_\.]*@[a-z]+\.[a-z]{1,3}$'

for _ in range(int(input())):

    parsed_address = email.utils.parseaddr(input())

    if re.search(pattern, parsed_address[1], re.I):
        print(email.utils.formataddr(parsed_address))