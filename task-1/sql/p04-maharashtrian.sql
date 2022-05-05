SELECT count(*) AS 'Marathi Cities' FROM city
WHERE District = 'Maharashtra' AND CountryCode = 'IND'; -- CountryCode only required for being extra sure

/*
+----------------+
| Marathi Cities |
+----------------+
|             35 |
+----------------+
*/

