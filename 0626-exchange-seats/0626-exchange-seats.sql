# Write your MySQL query statement below
SELECT
    CASE
        WHEN
            id = (SELECT MAX(id) FROM seat) AND mod(id, 2) = 1
            THEN id
        WHEN
            mod(id, 2) = 0
            THEN id - 1
        ELSE
            id + 1
    END AS id, student
FROM seat
ORDER BY id