-- Write an SQL query to find the employees who earn more than their managers.

SELECT
    E1.name AS Employee
FROM
    Employee AS E1, Employee AS E2
WHERE
    E1.managerId IS NOT NULL 
    AND
    E1.managerId = E2.id
    AND
    E1.salary > E2.salary

/*
Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
*/