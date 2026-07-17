# Write your MySQL query statement below
SELECT firstName, LastName, city, state
FROM person LEFT JOIN address ON person.personId = address.personId