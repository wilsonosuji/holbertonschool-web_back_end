-- 2. Best band ever!
-- this SQL script ranks country origins of band by number of fans
SELECT origin, sum(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
