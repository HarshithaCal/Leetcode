SELECT 
    e2.reports_to AS employee_id,  
    (SELECT e1.name 
     FROM Employees e1 
     WHERE e1.employee_id = e2.reports_to) AS name,
    COUNT(e2.reports_to) AS reports_count, 
    ROUND(AVG(e2.age), 0) AS average_age
FROM Employees e2
GROUP BY e2.reports_to
HAVING COUNT(e2.reports_to) > 0
ORDER BY e2.reports_to


