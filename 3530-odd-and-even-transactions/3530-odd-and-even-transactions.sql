select transaction_date, 
SUM(CASE WHEN amount %2 <> 0 THEN amount
ELSE 0
END) As odd_sum,

SUM(CASE WHEN amount %2 = 0 THEN amount
ELSE 0
END) As even_sum

FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date