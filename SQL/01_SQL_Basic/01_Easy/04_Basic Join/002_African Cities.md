## 002 - African Cities
<br>

### Problem
Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.


### Input Format

The `CITY ` table is described as follows :

|  Field | Type |
|---|---|
| ID  | NUMBER |
| NAME | VARCHAR2(17)   |
| COUNTRYCODE  | VARCHAR2(3)  |
| DISTRICT |  VARCHAR2(20) |
| POPULATION | NUMBER |

<br>

The `COUNTRY ` table is described as follows :

|  Field | Type |
|---|---|
| CODE  | VARCHAR2(3)   |
| NAME | VARCHAR2(44)   |
| CONTINENT | VARCHAR2(13) |
| REGION  | VARCHAR2(25)  |
| SURFACEAREA | NUMBER |
| INDEPYEAR | VARCHAR2(5) |
| POPULATION | NUMBER |
| LIFEEXPENTENCY | VARCHAR2(4) |
| GNP | NUMBER |
| GNPOLD | VARCHAR2(9) |
| LOCALNAME | VARCHAR2(44) |
| GOVERNMENTFORM | VARCHAR2(44) |
| HEADOFSTATE | VARCHAR2(32) |
| CAPITAL | VARCHAR2(4) |
| CODE2 | VARCHAR2(2) |



<br>

---

### Solution


```SQL
select ci.name from city  ci
inner join
country co on ci.countrycode = co.code
where continent = 'africa';
```

<br>

**Output**

```
Qina
Warraq al-Arab
Kempton Park
Alberton
Klerksdorp
Uitenhage
Brakpan
Libreville
```