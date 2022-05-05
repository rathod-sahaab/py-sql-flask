SELECT Code, Name, Population FROM country
WHERE Population = (SELECT max(Population) from country);

/*
+------+-------+------------+
| Code | Name  | Population |
+------+-------+------------+
| CHN  | China | 1277558000 |
+------+-------+------------+
*/
