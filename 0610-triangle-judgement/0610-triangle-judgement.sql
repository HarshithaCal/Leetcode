# Write your MySQL query statement below
#sum of two sides > third side - all the combinations

-- SELECT x, y, z, 
--        CASE 
--            WHEN x + y > z AND x + z > y AND y + z > x 
--            THEN "Yes"
--            ELSE "No"
--        END AS triangle
-- FROM Triangle;


#Using IF statement in SELECT
select x, y, z,
if((x+y)>z AND (y+z)>x AND (x+z)>y, 'Yes', 'No') as triangle
from Triangle