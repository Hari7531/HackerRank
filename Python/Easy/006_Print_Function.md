# 6 - Print Function
## Task
Read an integer `N` .

Without using any string methods, try to print the following:
`123...N`

Note that "..." represents the values in between.

#### Input Format

The first line contains an integer `N`.


#### Output Format

Output the answer as explained in the task.

```
Sample Input :
3
```

```
Sample Output :
123
```


#### Given Code

```python
if __name__ == '__main__':
    n = int(input())
```

----

## Method 1
#### Using string
```python
if __name__ == '__main__':
    n = int(input())
    lst = ""
    for num in range(1, n+1):
      lst += str(num)
    print(lst)
```
## Method 2
#### Using List

```python
if __name__ == '__main__':
    n = int(input())
    lst = []
    for num in range(1, n+1):
      lst.append(str(num))
    print("".join(lst))
```
## Method 3
#### Using List comprehenssion

```python
if __name__ == '__main__':
    n = int(input())
    lst = [x for x in range(1,n+1)]
    print(*lst, sep="")
```
## Method 4
#### Using Join method
```python
if __name__ == '__main__':
    n = int(input())
    print("".join([str(x) for x in range(1,n+1)]))
```
## Method 5
#### Using range method

```python
if __name__ == '__main__':
    n = int(input())
    print(*range(1, n + 1), sep="")
```