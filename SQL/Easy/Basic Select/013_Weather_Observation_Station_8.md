## 13 - Weather Observation Station 8
<br>

## Problem
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.


## Input Format

The `STATION` table is described as follows :

![](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where `LAT_N` is the northern latitude and `LONG_W` is the western longitude.

<br>

---

## Solution


```SQL
select distinct city from station
where lower(left(city,1)) in ('a','e','i','o','u') and lower(right(city,1)) in ('a','e','i','o','u');
```

<br>

**Output**

```
Upperco
Aguanga
East China
East Irvine
Amo
Eleele
Oconee
Amazonia
Aliso Viejo
Andersonville
Arkadelphia
Eriline
Eastlake
Arispe
Ermine
Eufaula
Osborne
Elm Grove
Atlantic Mine
Oshtemo
Archie
Alpine
Ojai
Urbana
Alba
Eskridge
Ozona
Acme
```