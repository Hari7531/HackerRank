"001 - Map and Lambda Function"

"""
Problem
Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 0 being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Input Format

One line of input: an integer N.

Output Format

A list on a single line containing the cubes of the first N fibonacci numbers.

Sample Input 0

5
Sample Output 0

[0, 1, 1, 8, 27]

"""



cube = lambda x: x ** 3

def fibonacci(n):
    
    f = [0, 1]

    if n < 2:
        return f[:n]

    for i in range(n - 2):
        f.append(f[i] + f[i + 1])

    return f

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))