## be cautious in picking the user_id from the correct table

SELECT S.user_id, IFNULL(ROUND(SUM(C.action="Confirmed")/COUNT(*), 2), 0) AS confirmation_rate
FROM Confirmations AS C
RIGHT JOIN Signups AS S
ON C.user_id = S.user_id
GROUP BY S.user_id 
ORDER BY s.user_id