## 010 - Weather Observation Station 6
<br>

## Problem
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.


## Input Format

The `STATION` table is described as follows :

![](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where `LAT_N` is the northern latitude and `LONG_W` is the western longitude.

<br>

---

## Solution


```SQL
select distinct city from station
where lower(left(city,1)) in ('a','e','i','o','u');
```

<br>

**Output**

```
Arlington
Albany
Upperco
Aguanga
Odin
East China
Algonac
Onaway
Irvington
Arrowsmith
Udall
Oakfield
Elkton
East Irvine
Amo
Alanson
Eleele
Auburn
Oconee
Amazonia
Aliso Viejo
Andersonville
Eros
Arkadelphia
Eriline
Edgewater
East Haddam
Eastlake
Addison
Everton
Eustis
Arispe
Union Star
Ottertail
Ermine
Albion
Athens
Eufaula
Osage City
Andover
Osborne
Elm Grove
Atlantic Mine
Oshtemo
Archie
Olmitz
Allerton
Equality
Alpine
Ojai
Orange Park
Urbana
Ukiah
Alba
Esmond
Eureka Springs
Eskridge
Ozona
Orange City
Effingham
Alton
Agency
Anthony
Emmett
Acme
```