
## 017 - Higher Than 75 Marks
<br>

## Problem
Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending

## Input Format

The `STUDENTS` table is described as follows :


|  Column | Type |
|---|---|
| ID  | Integer |
| Name | String   |
| Marks  | Integer  |

The `Name` column only contains uppercase (A-Z) and lowercase (a-z) letters.


<br>

---

## Solution


```SQL
select name from students
where marks > 75
order by right(name,3), id;

```

<br>

**Output**

```
Stuart
Kristeen
Christene
Amina
Aamina
Priya
Heraldo
Scarlet
Julia
Salma
Britney
Priyanka
Samantha
Vivek
Belvet
Devil
Evil
```
