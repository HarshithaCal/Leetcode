# Write your MySQL query statement below

SELECT EmployeeUNI.unique_id, Employees.name FROM Employees
LEFT JOIN EmployeeUNI #Left Outer join also works. Both are same.
ON EmployeeUNI.id = Employees.id;