# Write your MySQL query statement below

SELECT e1.employee_id FROM Employees e1
WHERE e1.salary < 30000 
AND e1.manager_id
    NOT IN 
        (SELECT DISTINCT e2.employee_id FROM Employees e2) #list of employees still present in the company
ORDER BY e1.employee_id;


