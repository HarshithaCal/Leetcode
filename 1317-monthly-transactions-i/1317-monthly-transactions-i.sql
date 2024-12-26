SELECT 
-- LEFT(trans_date, 7) AS month,
DATE_FORMAT(trans_date, '%Y-%m') AS month,
-- SUBSTR(trans_date,1,7) as month,
country,
COUNT(*) as trans_count,
SUM(state = "approved") as approved_count,
-- SUM(CASE WHEN state = 'approved' then 1 else 0 END) as approved_count, 
SUM(amount) as trans_total_amount,
SUM((state = "approved")*amount) AS approved_total_amount
-- SUM(CASE WHEN state = 'approved' then amount else 0 END) as approved_total_amount
-- SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM Transactions 
GROUP BY month, country;