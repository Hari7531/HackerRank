## 001 - Binary Tree Nodes
<br>

## Problem
You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.


The `BST` table is described as follows :

|  Column | Type |
|---|---|
| N  | Integer |
| P | Integer |

<br>



Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

`Root`: If node is root node.
`Leaf`: If node is leaf node.
`Inner`: If node is neither root nor leaf node.

## Input Format

The `BST` table is described as follows :

|  N | P |
|---|---|
| 1  | 2 |
| 3 | 2 |
| 6 | 8 |
| 9 | 8 |
| 2 | 5 |
| 8 | 5 |
| 5 | null |
<br>

`Sample Output`

1 Leaf
2 Inner
3 Leaf
5 Root
6 Leaf
8 Inner
9 Leaf
<br>

---

## Solution


```SQL
`Method-1`

SELECT N,
CASE
   WHEN P IS NULL THEN 'Root'
   WHEN (SELECT COUNT(*) FROM BST WHERE B.N=P)>0 THEN 'Inner'
   ELSE 'Leaf'
END AS BST_TYPE
FROM BST B
ORDER BY N;
```
```SQL
<br>
`Method-2`

SELECT N,
  IF( P IS NULL, 'Root', 
     IF ((SELECT COUNT(*) FROM BST WHERE B.N = P) > 0, 'Inner', 'Leaf')
    ) AS BST_TYPE
FROM BST B
ORDER BY N;
```

<br>

**Output**

```
1 Leaf
2 Inner
3 Leaf
4 Inner
5 Leaf
6 Inner
7 Leaf
8 Leaf
9 Inner
10 Leaf
11 Inner
12 Leaf
13 Inner
14 Leaf
15 Root
```