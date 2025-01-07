-- Subqueries
-- select d.name AS Department, e.name AS Employee, e.salary AS Salary
-- FROM Department d
-- JOIN Employee e
-- ON e.departmentId = d.id
-- WHERE (d.id, salary) IN (
--                                 SELECT departmentId, MAX(salary) 
--                                 FROM Employee
--                                 GROUP BY departmentId
--                             )


-- CTE - Approach 1
WITH cte AS
(
    SELECT departmentId, MAX(salary) 
    FROM Employee
    GROUP BY departmentId 
)

SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Department d
JOIN Employee e
ON e.departmentId = d.id
WHERE (d.id, salary) IN (SELECT * FROM cte)




