## 003 - Weather Observation Station 20

## 📘 Problem Statement

A **median** is defined as a number separating the higher half of a data set from the lower half.  

Write a SQL query to **find the median of Northern Latitudes (`LAT_N`)** from the `STATION` table and **round your answer to 4 decimal places**.

---

### ⚙️ Notes

- Median = middle value of a sorted dataset.  
- Odd number of rows → middle value.  
- Even number of rows → average of the two middle values.  

---

## 🧾 Table Schema

### **STATION**
| Column | Type |
|:--|:--|
| ID | NUMBER |
| CITY | VARCHAR2(21) |
| STATE | VARCHAR2(2) |
| LAT_N | NUMBER |
| LONG_W | NUMBER |

---

## 🧩 Sample Input

| ID | CITY      | STATE | LAT_N | LONG_W |
|----|-----------|-------|-------|--------|
| 1  | CityA     | AA    | 10.5  | 20.1   |
| 2  | CityB     | BB    | 15.2  | 25.3   |
| 3  | CityC     | CC    | 18.7  | 30.2   |
| 4  | CityD     | DD    | 22.0  | 35.1   |
| 5  | CityE     | EE    | 24.3  | 40.0   |

---

## 🧮 Sample Output

18.7000


---

## ✅ SQL Solution (Using CTE + Window Functions)

```sql
WITH ordered AS (
    SELECT
        LAT_N,
        ROW_NUMBER() OVER (ORDER BY LAT_N) AS rn,
        COUNT(*) OVER () AS total_count
    FROM STATION
)
SELECT
    ROUND(AVG(LAT_N), 4) AS median
FROM ordered
WHERE rn IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));


