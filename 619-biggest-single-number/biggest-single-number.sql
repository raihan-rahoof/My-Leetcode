-- Write your PostgreSQL query statement below
SELECT MAX(num) as num from ( select num from MyNumbers group by num having count(*)=1)