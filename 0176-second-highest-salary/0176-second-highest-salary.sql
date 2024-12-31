SELECT 
    IFNULL(
        (SELECT DISTINCT salary AS SecondHighestSalary
         FROM Employee
         GROUP BY salary
         ORDER BY salary DESC
         LIMIT 1 
         OFFSET 1),
        NULL
    ) AS SecondHighestSalary;
