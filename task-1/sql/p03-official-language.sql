SELECT country.Name as Country, Language FROM countrylanguage LEFT JOIN country ON country.Code = CountryCode
WHERE IsOfficial = 'T' AND Percentage >= 80 AND Percentage <= 90;

/*
+----------------------+-------------+
| Country              | Language    |
+----------------------+-------------+
| Netherlands Antilles | Papiamento  |
| Australia            | English     |
| Azerbaijan           | Azerbaijani |
| Bulgaria             | Bulgariana  |
| Bolivia              | Spanish     |
| Chile                | Spanish     |
| Czech Republic       | Czech       |
| Algeria              | Arabic      |
| Gibraltar            | English     |
| Greenland            | Greenlandic |
| Cambodia             | Khmer       |
| Liechtenstein        | German      |
| Lesotho              | Sotho       |
| Lithuania            | Lithuanian  |
| New Zealand          | English     |
| Palau                | Palau       |
| Russian Federation   | Russian     |
| Slovakia             | Slovak      |
| Slovenia             | Slovene     |
| Sweden               | Swedish     |
| Swaziland            | Swazi       |
| Syria                | Arabic      |
| Turkey               | Turkish     |
| United States        | English     |
| Virgin Islands, U.S. | English     |
| Vietnam              | Vietnamese  |
+----------------------+-------------+
*/
