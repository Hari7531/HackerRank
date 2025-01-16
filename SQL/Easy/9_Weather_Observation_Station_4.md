## 9 - Weather Observation Station 4
<br>

## Problem
Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows:


## Input Format

The `STATION` table is described as follows :

![](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where `LAT_N` is the northern latitude and `LONG_W` is the western longitude.

<br>

---

## Solution


```SQL
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) AS City_diff_count FROM STATION;
```

<br>

**Output**

```
13
```