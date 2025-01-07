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
-- WITH cte AS
-- (
--     SELECT departmentId, MAX(salary) 
--     FROM Employee
--     GROUP BY departmentId 
-- )

-- SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
-- FROM Department d
-- JOIN Employee e
-- ON e.departmentId = d.id
-- WHERE (d.id, salary) IN (SELECT * FROM cte)


#CTE approach 2 - more versatile
#cte - is ranking the employees based on their salary in each department
with cte as (
    select name, salary, departmentId,
    dense_rank() over(  partition by departmentId 
                        order by 
                        salary desc) as ranking 
                        #dense rank as same salary - same rank and need not skip the ranking for the next one
    from Employee
)

select d.name as Department, cte.name as Employee, cte.salary as Salary
from cte 
join Department d
on cte.departmentId = d.id
where cte.ranking = 1;





