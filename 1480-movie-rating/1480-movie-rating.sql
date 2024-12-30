(
    SELECT name AS results
    FROM MovieRating
    JOIN Users ON MovieRating.user_id = Users.user_id
    GROUP BY MovieRating.user_id
    ORDER BY COUNT(MovieRating.movie_id) DESC, name ASC
    LIMIT 1
)
UNION ALL #Stacks the second subselect below the first one (instead of merging duplicates like UNION would).
(
    SELECT title AS results
    FROM Movies M
    JOIN MovieRating MR ON M.movie_id = MR.movie_id
    WHERE SUBSTRING(created_at, 1, 7) = '2020-02'
    GROUP BY title
    ORDER BY AVG(rating) DESC, title ASC
    LIMIT 1
);