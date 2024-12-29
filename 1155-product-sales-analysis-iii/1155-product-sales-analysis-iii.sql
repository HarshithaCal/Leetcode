SELECT product_id, year AS first_year, quantity, price 
FROM Sales 
WHERE (product_id, year) IN (
    SELECT product_id, MIN(year) AS year 
    FROM Sales 
    GROUP BY product_id
  );


-- SELECT product_id, year as first_year, quantity, price
-- FROM Sales
-- WHERE year = (
--     SELECT MIN(year)
--     FROM Sales AS s2
--     WHERE Sales.product_id = s2.product_id
-- );
