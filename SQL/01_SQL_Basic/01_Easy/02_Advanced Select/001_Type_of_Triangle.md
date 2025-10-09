
## 001 - Type of Triangle
<br>

## Problem
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

<br>

Equilateral: It's a triangle with 3 sides of equal length.<br>
Isosceles: It's a triangle with 2 sides of equal length.<br>
Scalene: It's a triangle with 3 sides of differing lengths.<br>
Not A Triangle: The given values of A, B, and C don't form a triangle.<br>

## Input Format

The `TRIANGLES ` table is described as follows :


|  Column | Type |
|---|---|
| A  | Integer |
| B | Integer   |
| C  | Integer  |

Each row in the table denotes the lengths of each of a triangle's three sides.

<br>

## Sample Input

|  A | B | C |
|---|---|---|
| 20 | 20 | 23 |
| 20 | 20   | 20 |
| 20  | 21  | 22 |
| 13  | 14  | 30 |

## Sample Output

Isosceles <br>
Equilateral <br>
Scalene <br>
Not A Triangle <br>

## Solution


```SQL
SELECT
    CASE
        when A+B <= C or A+C <= B or B+C <= A then "Not A Triangle"
        when A=B and B=C then "Equilateral"
        when A=B or B=C or C=A then "Isosceles"
        when A<>B and B<>C then "Scalene"

    END  AS triangles_type FROM TRIANGLES;

```

<br>

**Output**

```
Equilateral
Equilateral
Isosceles
Equilateral
Isosceles
Equilateral
Scalene
Not A Triangle
Scalene
Scalene
Scalene
Not A Triangle
Not A Triangle
Scalene
Equilateral
```
