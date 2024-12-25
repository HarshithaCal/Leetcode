-- SELECT * FROM Signups AS S
-- LEFT JOIN Confirmations AS C
-- ON S.user_id = C.user_id

SELECT S.user_id, IFNULL(ROUND(SUM(C.action="Confirmed")/COUNT(*), 2), 0) AS confirmation_rate
FROM Confirmations AS C
RIGHT JOIN Signups AS S
ON C.user_id = S.user_id
GROUP BY S.user_id 
ORDER BY s.user_id