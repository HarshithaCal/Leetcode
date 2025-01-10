select u.user_id AS buyer_id, u.join_date,
COUNT(IF(YEAR(o.order_date)=2019,1,NULL)) AS orders_in_2019 ## key!!
FROM Orders o
RIGHT JOIN Users u
ON u.user_id = o.buyer_id
-- WHERE LEFT(order_date, 4) = "2019"   ###### this is the issue to print 0's
GROUP BY u.user_id, u.join_date
