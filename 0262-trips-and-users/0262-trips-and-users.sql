##drivers
WITH cte AS  
( SELECT id, client_id, driver_id, status, request_at FROM Trips t
-- ud.role, ud.users_id, status, request_at, id, client_id, driver_id FROM Trips t
JOIN Users ud
ON t.driver_id = ud.users_id
AND ud.role = "driver"
AND ud.banned = "No"
WHERE DAY(request_at) BETWEEN "1" AND "3"
AND t.client_id IN (select users_id FROM Users WHERE banned = "No" AND role= "client")
  ),

total AS
(
select id, request_at, COUNT(request_at) AS total_count fROM cte
-- WHERE status = "completed"
GROUP BY request_at
),

cancelled AS
(
select id, request_at, COUNT(request_at) AS cancelled_count fROM cte
WHERE status != "completed"
GROUP BY request_at
)

SELECT DATE(t.request_at) AS 'Day',
COALESCE(ROUND(cancelled_count/total_count, 2), 0) AS 'Cancellation Rate' 
FROM total t
LEFT JOIN cancelled c
ON c.request_at = t.request_at






