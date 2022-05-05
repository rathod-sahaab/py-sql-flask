SELECT Language, COUNT(CountryCode) as Countries FROM countrylanguage
GROUP BY Language
ORDER BY Countries DESC
LIMIT 1;

/*
+----------+-----------+
| Language | Countries |
+----------+-----------+
| English  |        60 |
+----------+-----------+
*/

