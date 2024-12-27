SELECT query_name, 
-- ROUND(SUM(rating/position)/COUNT(rating),2) AS quality,
round(avg(rating / position), 2) as quality,
ROUND(100 * SUM(IF(rating<3, 1, 0))/COUNT(*), 2) AS poor_query_percentage
-- round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
FROM Queries
GROUP BY query_name;
