-- select 
--     case  
--         when id = (select max(id) from seat) and id % 2 = 1
--             then id

--         when id % 2 = 1
--             then id + 1

--         when id % 2 = 0
--             then id - 1
--     end as id,
--     student
-- from seat
-- order by id;

SELECT 
    id,
    CASE
        WHEN id % 2 = 0 THEN LAG(student) OVER(ORDER BY id)
        ELSE COALESCE(LEAD(student) OVER(ORDER BY id), student)
    END AS student
FROM Seat
