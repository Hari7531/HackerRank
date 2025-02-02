"001 - Polar Coordinates"

"""
Task 
You are given a complex z.Your task is to convert it to polar coordinates.

Input Format
A single line containing the complex number z. Note: complex() function can be used in 
python to convert the input as a complex number.

Output Format
Output two lines: 
The first line should contain the value of r. 
The second line should contain the value of θ.

Sample Input
1+2j

Sample Output
2.23606797749979 
1.1071487177940904
"""
#Method 1
import cmath

modulus, argument = cmath.polar(complex(input()))
#modulus(r)
print(modulus)
#argument(theta)
print(argument)
# Method 2

from cmath import phase
complx = complex(input())
print(abs(complex(complx.real,complx.imag)))
print(phase(complex(complx.real,complx.imag)))