## 004 - Average Population
<br>

## Problem
Query the average population for all cities in CITY, rounded down to the nearest integer.


## Input Format

The `CITY` table is described as follows :


|  Field | Type |
|---|---|
| ID  | NUMBER |
| NAME | VARCHAR2(17)   |
| COUNTRYCODE  | VARCHAR2(3)  |
| DISTRICT |  VARCHAR2(20) |
| POPULATION | NUMBER |


<br>

---

## Solution


```SQL
select round(avg(population)) from city;

```

<br>

**Output**

```
454250
```