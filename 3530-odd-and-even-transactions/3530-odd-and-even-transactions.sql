select  
        transaction_date,
        coalesce(sum(case when mod(amount,2)=1 then amount end),0) as odd_sum,   #coalesce() fills NULL with the value
        coalesce(sum(case when mod(amount,2)=0 then amount end),0) as even_sum
    from transactions
    group by 1  #col number
    order by 1

#### Using IF statement
-- SELECT transaction_date,
--  sum(if(amount % 2 = 1, amount, 0)) as odd_sum,
--  sum(if(amount % 2 = 0, amount, 0)) as even_sum
-- from transactions
-- GROUP BY transaction_date 
-- ORDER BY transaction_date;



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