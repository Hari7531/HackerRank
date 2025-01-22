# 009 - Weather Observation Station 2
<br>

## Problem

Query the following two values from the STATION table:

1.The sum of all values in LAT_N rounded to a scale of 2 decimal places.
2.The sum of all values in LONG_W rounded to a scale of 2 decimal places.


## Input Format

The `STATION` table is described as follows :

![](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where `LAT_N` is the northern latitude and `LONG_W` is the western longitude.

## Output Format

Your results must be in the form:

lat lon <br>
where `lat` is the sum of all values in LAT_N and `lon` is the sum of all values in LONG_W. 
Both results must be rounded to a scale of  decimal places.
---

## Solution


```SQL
select round(sum(lat_n),2),round(sum(long_w),2) from station;

```

<br>

**Output**

```
42850.04 47381.48
```