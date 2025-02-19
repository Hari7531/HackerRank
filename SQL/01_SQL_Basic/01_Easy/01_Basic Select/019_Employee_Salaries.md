## 019 - Employee Salaries
<br>

## Problem
Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than $2000 per month who have been employees for less than 10 months. Sort your result by ascending employee_id.

## Input Format

The `Employee` table is described as follows :


|  Column | Type |
|---|---|
| employee_id  | Integer |
| name | String   |
| months  | Integer  |
| salary  | Integer  |

where `employee_id` is an employee's ID number, `name` is their name, `months` is the total number of months they've been working for the company, and `salary` is their monthly salary.


<br>

---

## Solution


```SQL
select name from employee
where salary > 2000 and months < 10
order by employee_id;

```

<br>

**Output**

```
Rose 
Patrick 
Lisa 
Amy 
Pamela 
Jennifer 
Julia 
Kevin 
Paul 
Donna 
Michelle 
Christina 
Brandon 
Joseph 
Jesse 
Paula 
Louise 
Evelyn 
Emily 
Jonathan 
Nancy 
Benjamin 
Roy 
Diana 
Christine 
```
