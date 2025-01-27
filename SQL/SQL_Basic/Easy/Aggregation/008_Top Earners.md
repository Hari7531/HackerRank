## 008 - Top Earners
<br>

## Problem
We define an employee's total earnings to be their (monthly salary*months worked), and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.

## Input Format

The `EMPLOYEES` table is described as follows :


|  Column | Type |
|---|---|
| employee_id  | Integer |
| name | String  |
| months  | Integer |
| salary  | Integer |


where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is the their monthly salary.


<br>

---

## Solution


```SQL
select (months*salary) as total_earning,count(*) from employee
group by total_earning order by total_earning desc limit 1;

```

<br>

**Output**

```
108064 7 
```