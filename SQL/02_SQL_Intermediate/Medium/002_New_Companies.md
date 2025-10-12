## 002 - New Companies
<br>
## 📘 Problem Statement

Amber's conglomerate corporation just acquired some new companies.  
Each of the companies follows this hierarchy:

Company → Lead_Manager → Senior_Manager → Manager → Employee


Given the table schemas below, write a query to print the following for each company:

- **company_code**
- **founder**
- **total number of lead managers**
- **total number of senior managers**
- **total number of managers**
- **total number of employees**

Order your output by **ascending company_code**.

---

### ⚙️ Notes

- The tables may contain **duplicate records**.
- The `company_code` is a **string**, so sorting should be **lexicographical**, not numeric.  
  For example: `C_1`, `C_10`, `C_2` → **C_1**, **C_10**, **C_2**.

---

## 🧾 Table Schemas

### **Company**
| Column | Type |
|:--|:--|
| company_code | String |
| founder | String |

### **Lead_Manager**
| Column | Type |
|:--|:--|
| lead_manager_code | String |
| company_code | String |

### **Senior_Manager**
| Column | Type |
|:--|:--|
| senior_manager_code | String |
| lead_manager_code | String |
| company_code | String |

### **Manager**
| Column | Type |
|:--|:--|
| manager_code | String |
| senior_manager_code | String |
| lead_manager_code | String |
| company_code | String |

### **Employee**
| Column | Type |
|:--|:--|
| employee_code | String |
| manager_code | String |
| senior_manager_code | String |
| lead_manager_code | String |
| company_code | String |

---

## 🧩 Sample Input

### **Company**
| company_code | founder |
|---|---|
| C1 | Monika |
| C2 | Samantha |

### **Lead_Manager**
| lead_manager_code | company_code |
|---|---|
| LM1 | C1 |
| LM2 | C2 |

### **Senior_Manager**
| senior_manager_code | lead_manager_code | company_code |
|---|---|---|
| SM1 | LM1 | C1 |
| SM2 | LM1 | C1 |
| SM3 | LM2 | C2 |

### **Manager**
| manager_code | senior_manager_code | lead_manager_code | company_code |
|---|---|---|---|
| M1 | SM1 | LM1 | C1 |
| M2 | SM3 | LM2 | C2 |
| M3 | SM3 | LM2 | C2 |

### **Employee**
| employee_code | manager_code | senior_manager_code | lead_manager_code | company_code |
|---|---|---|---|---|
| E1 | M1 | SM1 | LM1 | C1 |
| E2 | M1 | SM1 | LM1 | C1 |
| E3 | M2 | SM3 | LM2 | C2 |
| E4 | M3 | SM3 | LM2 | C2 |

---

## 🧮 Sample Output

C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2


---

## 🧠 Explanation

In **company C1**,  
- Lead managers: **LM1 (1)**  
- Senior managers: **SM1, SM2 (2)**  
- Managers: **M1 (1)**  
- Employees: **E1, E2 (2)**  

In **company C2**,  
- Lead managers: **LM2 (1)**  
- Senior managers: **SM3 (1)**  
- Managers: **M2, M3 (2)**  
- Employees: **E3, E4 (2)**  

---

## ✅ SQL Solution

```sql
SELECT
    c.company_code,
    c.founder,
    COUNT(DISTINCT l.lead_manager_code) AS lead_manager_count,
    COUNT(DISTINCT s.senior_manager_code) AS senior_manager_count,
    COUNT(DISTINCT m.manager_code) AS manager_count,
    COUNT(DISTINCT e.employee_code) AS employee_count
FROM Company c
LEFT JOIN Lead_Manager l
    ON c.company_code = l.company_code
LEFT JOIN Senior_Manager s
    ON c.company_code = s.company_code
LEFT JOIN Manager m
    ON c.company_code = m.company_code
LEFT JOIN Employee e
    ON c.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;
