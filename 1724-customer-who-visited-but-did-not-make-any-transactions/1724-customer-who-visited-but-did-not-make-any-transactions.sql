SELECT  c.customer_id, COUNT(*) as count_no_trans from Visits c
LEFT JOIN Transactions AS t ON c.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY c.customer_id 


