# Write your MySQL query statement below
SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM requestAccepted
UNION ALL
    SELECT accepter_id FROM requestAccepted
) AS friend_request
GROUP BY id
ORDER BY num DESC
LIMIT 1