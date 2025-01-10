select Department, sub.name AS Employee , salary AS Salary FROM (
    select d.name AS Department, e.name, e.salary, 
    DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS ranks FROM Employee e
    JOIN Department d
    ON d.id = e.departmentId
) AS sub

WHERE sub.ranks <4

