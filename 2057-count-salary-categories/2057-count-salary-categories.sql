-- # Write your MySQL query statement below
-- SELECT CASE WHEN income < 20000 THEN "Low Salary"
--             WHEN income between 2000 AND 5000 THEN "Average Salary"
--             ELSE "High Salary" 
--             END AS category,

--         COUNT(*) as accounts_count
-- FROM Accounts
-- GROUP BY category
#here, directly using CASE doesn't work as it doesn't create a case category if there is no match so use UNION

SELECT "Low Salary" as category, sum(if(income<20000,1,0)) AS accounts_count FROM Accounts
union
SELECT "Average Salary" as category, sum(if(income>=20000 and income<=50000,1,0)) AS accounts_count FROM Accounts
union
SELECT "High Salary" as category, sum(if(income>50000,1,0)) AS accounts_count FROM Accounts
