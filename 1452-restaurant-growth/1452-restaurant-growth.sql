select visited_on, 
SUM(amount)
    OVER(ORDER BY visited_on ASC
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ) AS amount,
ROUND(AVG(amount)
    OVER( ORDER BY visited_on ASC
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ), 2) AS average_amount
FROM (
    select visited_on, SUM(amount) AS amount FROM Customer
    GROUP BY visited_on
        ) AS subQuery
ORDER BY visited_on
LIMIT 6, 9999


