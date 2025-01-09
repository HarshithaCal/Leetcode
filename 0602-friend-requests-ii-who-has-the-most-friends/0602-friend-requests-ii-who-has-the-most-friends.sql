# Write your MySQL query statement below

-- select id, max(`sum(counter)`) AS num FROM 
-- (
    with cte AS
    (
select id, sum(counter) AS total_requests FROM (
select requester_id as id , COUNT(requester_id) AS counter 
FROM RequestAccepted 
GROUP BY id

UNION ALL #we want duplicates!!!

select accepter_id as id, COUNT(accepter_id) AS counter
FROM RequestAccepted 
GROUP BY id
) as sub
GROUP BY id
    )

select id, total_requests AS num from cte
order by num desc
limit 1