select d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Department d
JOIN Employee e
ON e.departmentId = d.id
WHERE (d.id, salary) IN (
                                SELECT departmentId, MAX(salary) 
                                FROM Employee
                                GROUP BY departmentId
                            )
