## 021 - Weather Observation Station 17
<br>

## Problem
Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to 4 decimal places.

## Input Format

The `STATION` table is described as follows :


|  Field | Type |
|---|---|
| ID  | NUMBER |
| CITY | VARCHAR2(21)   |
| STATE  | VARCHAR2(2)  |
| LAT_N |  NUMBER |
| LONG_W | NUMBER |

where `LAT_N` is the northern latitude and `LONG_W` is the western longitude.


<br>

---

## Solution


```SQL
select round(long_w,4) from station
where lat_n > 38.770 
order by lat_n limit 1;

```

<br>

**Output**

```
70.1378
```
