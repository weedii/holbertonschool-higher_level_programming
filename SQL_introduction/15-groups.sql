--
SELECT score, COUNT(score) as score
FROM second_table
GROUP BY score;