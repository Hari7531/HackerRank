"003 - Check Strict Superset"

"""
You are given a set A and n other sets. 
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.

Input Format
The first line contains the space separated elements of set A. 
The second line contains integer n, the number of other sets. 
The next n lines contains the space separated elements of the other sets.

Output Format
Print True if set A is a strict superset of all other N sets. Otherwise, print False.

Sample Input:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output:
False
"""
# Method 1:
a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))

# Method 2:
s = set(map(int, input().split(' ')))
res = "True"
r = int(input())
for _ in range(r):
    t = set(map(int, input().split(' ')))
    if s.issuperset(t):
        res = "True"
    else:
        res = "False"
        break

print(res) 