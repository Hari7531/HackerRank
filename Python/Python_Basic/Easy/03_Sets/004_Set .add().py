"004 - Set .add()"

"""
Task
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number 
of distinct country stamps in her collection. She asked for your help. You pick the 
stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.

Input Format
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from. 

Output Format
Output the total number of distinct country stamps on a single line.

Sample Input
7
UK
China
USA
France
New Zealand
UK
France 

Sample Output
5

Explanation
UK and France repeat twice. Hence, the total number of distinct country stamps is 5(five).
"""
# Method 1
n = int(input())
Set = set()
for i in range(n):
    Set.add(input())
print(len(Set))

# Method 2

if __name__ == '__main__':
    s = set()

    for _ in range(int(input())):
        s.add(input())

    print(len(s))

# Method 3

n = int(input())
stamps = set()
while n > 0:
    stamps.add(input())
    n -= 1
print(len(stamps))