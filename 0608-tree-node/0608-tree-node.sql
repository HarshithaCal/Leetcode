#Hackerrank question

select id,
CASE WHEN p_id IS null THEN "Root" 

     WHEN id IN (
        SELECT DISTINCT p_id FROM Tree
     ) THEN "Inner"
     
     ELSE "Leaf"
END AS type
FROM Tree

