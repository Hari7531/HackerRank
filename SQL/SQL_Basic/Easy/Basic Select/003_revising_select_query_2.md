## 3 - Revising the Select Query 2
<br>

## Problem

Query the names of all American cities in `CITY` with populations larger than `120000`. The `COUNTRYCODE` for Ameria is `USA`.


## Input Format

The `CITY` table is described as follows :

![](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

---

## Solution

```SQL
select name from CITY 
where population > 120000 and COUNTRYCODE = "USA";
```

<br>

**Output**

```
Scottsdale
Corona
Concord
Cedar Rapids
```