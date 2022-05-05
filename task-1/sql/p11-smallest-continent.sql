SELECT Continent, sum(SurfaceArea) as Area FROM country
GROUP BY Continent
ORDER BY Area
LIMIT 1;

/*
+-----------+------------+
| Continent | Area       |
+-----------+------------+
| Oceania   | 8564294.00 |
+-----------+------------+
*/

