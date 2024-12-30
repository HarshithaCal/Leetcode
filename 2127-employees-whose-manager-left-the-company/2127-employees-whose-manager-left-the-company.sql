# Write your MySQL query statement below
#using subquery
-- SELECT e1.employee_id FROM Employees e1
-- WHERE e1.salary < 30000 
-- AND e1.manager_id
--     NOT IN 
--         (SELECT DISTINCT e2.employee_id FROM Employees e2) #list of employees still present in the company
-- ORDER BY e1.employee_id;

#using join
SELECT e1.employee_id
FROM Employees e1
LEFT JOIN Employees e2
ON e1.manager_id = e2.employee_id
WHERE e1.salary < 30000 AND e2.employee_id IS NULL AND e1.manager_id IS NOT NULL
ORDER BY employee_id;


