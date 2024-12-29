SELECT user_id, COUNT(follower_id) AS followers_count 
FROM Followers
group by user_id
ORDER BY user_id ASC;
