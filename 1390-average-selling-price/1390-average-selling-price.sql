SELECT p.product_id, 
IFNULL(ROUND(SUM(p.price*u.units)/SUM(u.units),2),0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id
#OR we can use this instead of where
AND u.purchase_date between p.start_date AND p.end_date
-- WHERE u.purchase_date between p.start_date AND p.end_date 
--                 OR u.purchase_date IS NULL #Eventhough LEFT JOIN is used WHERE misses the null cases.
GROUP BY p.product_id