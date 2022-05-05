SELECT count(*) as "Null Field Countries" FROM country
WHERE IndepYear IS NULL OR LifeExpectancy IS NULL OR GNP IS NULL OR HeadOfState IS NULL OR Capital IS NULL;

/*
+----------------------+
| Null Field Countries |
+----------------------+
|                   49 |
+----------------------+
*/
