# Write your MySQL query statement below
SELECT MAX(SALARY) AS SecondHighestSalary
FROM employee
WHERE SALARY < (
    SELECT MAX(SALARY)
    FROM employee
)