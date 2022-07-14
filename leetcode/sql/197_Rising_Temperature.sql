-- Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

SELECT
    wt1.id AS id
FROM
    Weather wt1, Weather wt2
WHERE
    wt1.temperature > wt2.temperature 
    AND
    DATEDIFF(wt1.recordDate , wt2.recordDate) = 1

/*
Example 1:

Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
*/