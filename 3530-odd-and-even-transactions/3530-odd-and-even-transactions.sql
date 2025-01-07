#### Using IF statement
SELECT transaction_date,
 sum(if(amount % 2 = 1, amount, 0)) as odd_sum,
 sum(if(amount % 2 = 0, amount, 0)) as even_sum
from transactions
GROUP BY transaction_date 
ORDER BY transaction_date;



### Using case statement
-- select transaction_date, 
-- SUM(CASE WHEN amount %2 <> 0 THEN amount
-- ELSE 0
-- END) As odd_sum,

-- SUM(CASE WHEN amount %2 = 0 THEN amount
-- ELSE 0
-- END) As even_sum

-- FROM transactions
-- GROUP BY transaction_date
-- ORDER BY transaction_date