# 8 - Weather Observation Station 3
<br>

## Problem

Query a list of `CITY` names from `STATION` for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.


## Input Format

The `STATION` table is described as follows :

![](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where `LAT_N` is the northern latitude and `LONG_W` is the western longitude.
---

## Solution


```SQL
SELECT DISTINCT CITY FROM STATION
 WHERE ID % 2 = 0;
```

<br>

**Output**

```
Aguanga
Alba
Albany
Amo
Andersonville
Archie
Athens
Atlantic Mine
Bainbridge
Baker
Bass Harbor
Bayville
Beaufort
Bellevue
Benedict
Bennington
Bentonville
Biggsville
Bison
Bono
Bowdon
Bridgton
Brownsdale
Brownstown
Bullhead City
Busby
Cahone
...
...
...
Yalaha
Yazoo City
Yellow Pine
Yuma
Zachary
```