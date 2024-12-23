# Write your MySQL query statement below
SELECT e1.name FROM Employee as e1
WHERE   
e1.id IN 
(SELECT managerId FROM Employee
GROUP BY managerId
HAVING COUNT(managerId) >= 5)