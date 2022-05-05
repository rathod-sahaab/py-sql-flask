CREATE VIEW english_north_american_countries AS
SELECT country.Code AS Code
FROM country LEFT JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE country.Continent = 'North America' AND countrylanguage.Language = 'English';

-- Total Cities in these English, North American countries
SELECT count(*)
FROM english_north_american_countries
LEFT JOIN city ON english_north_american_countries.Code = city.CountryCode;

DROP VIEW english_north_american_countries;

/*
+----------+
| count(*) |
+----------+
|      352 |
+----------+
*/

