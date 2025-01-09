WITH RankedResult AS
    (   select visited_on, 
        SUM(amount)
            OVER(ORDER BY visited_on ASC
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ) AS amount,
        ROUND(AVG(amount)
            OVER( ORDER BY visited_on ASC
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ), 2) AS average_amount,
        -- ROW_NUMBER() OVER (ORDER BY visited_on ASC) AS rn
        RANK() OVER (ORDER BY visited_on ASC) AS rn

        FROM (
            select visited_on, SUM(amount) AS amount FROM Customer
            GROUP BY visited_on
                ) AS subQuery
    )


SELECT visited_on, amount, average_amount
FROM RankedResult
WHERE rn >= 7
ORDER BY visited_on;



