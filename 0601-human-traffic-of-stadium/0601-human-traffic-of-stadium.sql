With new_table AS
(
    select id, visit_date, 
    LAG(people, 1, 0) OVER(order by id) AS visit1,
    LAG(people, 2, 0) OVER(order by id) AS visit2,
    people
    FROM Stadium
),
cte2 AS(
    SELECT id, visit_date, people FROM new_table
    WHERE visit1>= 100 AND visit2 >= 100 AND people >=100
)

select id, visit_date, people FROM Stadium
WHERE id IN (
    SELECT id FROM cte2
    UNION
    SELECT id - 1 FROM cte2
    UNION
    SELECT id - 2 FROM cte2
)
ORDER BY visit_date ASC;





