## 19 - Weather Observation Station 14
<br>

## Problem
Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to 4 decimal places.

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
/* select truncate(sum(lat_n),4) from station where lat_n between 38.7880 and 137.2345;*/


/*select round(sum(lat_n),4) from station where lat_n<137.2345;*/

select truncate(max(lat_n),4) from station where lat_n< 137.2345;

```

<br>

**Output**

```
137.0193
```
