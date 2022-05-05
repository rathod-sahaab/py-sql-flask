SELECT Name, Population FROM city
WHERE Population = (SELECT max(Population) from city);

/*
+-----------------+------------+
| Name            | Population |
+-----------------+------------+
| Mumbai (Bombay) |   10500000 |
+-----------------+------------+
*/
