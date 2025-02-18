"002 - Triangle Quest 2"

"""
You are given a positive integer .
Your task is to print a palindromic triangle of size .

For example, a palindromic triangle of size is:

1
121
12321
1234321
123454321
You can not take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

Note:
Using anything related to strings will give a score of .
Using more than one for-statement will give a score of .

Input Format

A single line of input containing the integer .

Constraints

Output Format

Print the palindromic triangle of size as explained above.

Sample Input

5
Sample Output

1
121
12321
1234321
123454321
Explanation:
The basic idea for palindromic triangle is, as soon as you reach the number equal to current iteration you go backtrack to the first number of your row i.e. if you are at i = 3, the row should stop at 3 (123) and then it should backtrack ( 12321).

Here, the question asks to derive the logic in one line (no nested loops allowed :( ), so, we observe a pattern here which repeats when you square 1, you get 1, when you square 11 you get 121, when you square 111 you get 12321 thus, we simply have to repeat this strategy, n (input) number of times.

For that very purpose, we have to derive our logic in such a way that our loop squares 1, 11, 111 over each iteration. Thus if we square the result of the value we get dividing (10**i— 1) where i is the iteration ( ex : 10¹–1 = 9, 10²-1 = 99, 10³-1 = 999) by 9 ( we use // to get the nearest whole number), we get 1, 11, 111. These results gets squared and returns the required output.

Happy Coding :)
"""
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i-1)//9)**2)
