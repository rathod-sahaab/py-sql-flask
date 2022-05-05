SELECT country.Name, CountryCode, COUNT(CountryCode) as Cities
FROM city LEFT JOIN country ON city.CountryCode = country.Code
GROUP BY CountryCode
ORDER BY Cities DESC
LIMIT 1;

/*
+-------+-------------+--------+
| Name  | CountryCode | Cities |
+-------+-------------+--------+
| China | CHN         |    363 |
+-------+-------------+--------+
*/
