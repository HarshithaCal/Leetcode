##drivers
-- WITH cte AS  
-- ( SELECT id, client_id, driver_id, status, request_at FROM Trips t
-- -- ud.role, ud.users_id, status, request_at, id, client_id, driver_id FROM Trips t
-- JOIN Users ud
-- ON t.driver_id = ud.users_id
-- AND ud.role = "driver"
-- AND ud.banned = "No"
-- WHERE DAY(request_at) BETWEEN "1" AND "3"
-- AND t.client_id IN (select users_id FROM Users WHERE banned = "No" AND role= "client")
--   ),

-- total AS
-- (
-- select id, request_at, COUNT(request_at) AS total_count fROM cte
-- -- WHERE status = "completed"
-- GROUP BY request_at
-- ),

-- cancelled AS
-- (
-- select id, request_at, COUNT(request_at) AS cancelled_count fROM cte
-- WHERE status != "completed"
-- GROUP BY request_at
-- )

-- SELECT DATE(t.request_at) AS 'Day',  # DATE() will fill the date if it's NULL - key!!!!
-- COALESCE(ROUND(cancelled_count/total_count, 2), 0) AS 'Cancellation Rate'  #Replace the NUll with 0's
-- FROM total t
-- LEFT JOIN cancelled c #LEFT JOIN to get the days with cancellation_rate = 0
-- ON c.request_at = t.request_at

#Different approach from the Editorial:
SELECT 
  request_at AS Day, 
  ROUND(
    SUM(status != 'completed') / COUNT(*), 
    2
  ) AS 'Cancellation Rate' 
FROM 
  Trips 
  LEFT JOIN Users AS Clients ON Trips.client_id = Clients.users_id 
  LEFT JOIN Users AS Drivers ON Trips.driver_id = Drivers.users_id 
WHERE 
  Clients.banned = 'No' 
  AND Drivers.banned = 'No' 
  AND request_at BETWEEN '2013-10-01' 
  AND '2013-10-03' 
GROUP BY 
  Day






