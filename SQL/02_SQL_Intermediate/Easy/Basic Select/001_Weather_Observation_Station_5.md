## 001 - Weather Observation Station 5
<br>

## Problem
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.


## Input Format

The `STATION` table is described as follows :

|  Field | Type |
|---|---|
| ID  | NUMBER |
| CITY | VARCHAR2(21)   |
| STATE  | VARCHAR2(2)  |
| LAT_N | NUMBER |
| LONG_W | NUMBER |

<br>

where `LAT_N` is the northern latitude and `LONG_W` is the western longitude.

<br>

---

## Solution


```SQL
#Method-1
-- Shortest city
select CITY, length(CITY) from STATION order by length(CITY), CITY limit 1;
-- Longest city
select CITY, length(CITY) from STATION order by length(CITY) desc, CITY limit 1;

#Method-2

-- Shortest city
(
    SELECT CITY, LENGTH(CITY) AS city_name_length
    FROM STATION
    ORDER BY LENGTH(CITY), CITY
    LIMIT 1
)
UNION ALL
-- Longest city
(
    SELECT CITY, LENGTH(CITY) AS city_name_length
    FROM STATION
    ORDER BY LENGTH(CITY) DESC, CITY
    LIMIT 1
);

#Method-3

SELECT CITY, name_length
FROM (
    SELECT 
        CITY,
        LENGTH(CITY) AS name_length,
        ROW_NUMBER() OVER (ORDER BY LENGTH(CITY), CITY) AS rn_shortest,
        ROW_NUMBER() OVER (ORDER BY LENGTH(CITY) DESC, CITY) AS rn_longest
    FROM STATION
) AS t
WHERE rn_shortest = 1 OR rn_longest = 1;
```

<br>

**Output**

```
Amo 3
Marine On Saint Croix 21
```