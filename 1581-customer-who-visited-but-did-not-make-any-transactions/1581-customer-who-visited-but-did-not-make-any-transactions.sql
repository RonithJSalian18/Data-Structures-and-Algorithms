# Write your MySQL query statement below
SELECT customer_id, COUNT(DISTINCT visit_id) as count_no_trans
FROM visits
WHERE visit_id NOT IN (
    SELECT visit_id FROM transactions
)
GROUP BY customer_id