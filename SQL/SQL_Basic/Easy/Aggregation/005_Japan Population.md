## 005 - Japan Population
<br>

## Problem
Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.


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
select sum(population) from city
where countrycode = 'jpn';

```

<br>

**Output**

```
879196
```