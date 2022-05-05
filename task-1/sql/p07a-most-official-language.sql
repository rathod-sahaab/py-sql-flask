SELECT Language, sum(CASE WHEN IsOfficial = 'T' THEN 1 ELSE 0 END) as official_in FROM countrylanguage
GROUP BY Language
ORDER BY official_in DESC
LIMIT 1;
-- can use max with views for optimisation

/*
+----------+-------------+
| Language | official_in |
+----------+-------------+
| English  |          44 |
+----------+-------------+
*/
