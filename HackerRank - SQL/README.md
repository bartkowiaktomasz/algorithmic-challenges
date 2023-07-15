# HackeRank - SQL
Solutions to [**HackerRank SQL**](https://www.hackerrank.com/domains/sql)

# Easy

### Revisiting the SQL Query I
> Query all columns for all American cities in the CITY table with populations larger than 100000.

```sql
SELECT * FROM city WHERE CountryCode = 'USA' AND POPULATION > 100000;
```

### Revisiting the SQL Query II
> Query the NAME field for all American cities in the CITY table with populations larger than 120000. 

```sql
SELECT name FROM CITY where POPULATION > 120000 AND COUNTRYCODE = 'USA';
```

### Select All
> Query all columns (attributes) for every row in the CITY table.

```sql
SELECT * FROM CITY;
```

### Select By ID
> Query all columns for a city in CITY with the ID 1661.

```sql
SELECT * FROM CITY WHERE ID = 1661;
```

### Japanese Cities' Attributes
> Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

```sql
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';
```

### Japanese Cities' Names
> Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.


```sql
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN';
```

### Weather Observation Station 1
> Query a list of CITY and STATE from the STATION table.

```sql
SELECT CITY, STATE FROM STATION;
```

### Weather Observation Station 3
> Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.

```sql
SELECT DISTINCT(CITY) FROM STATION WHERE MOD(ID, 2) = 0;
```

### Weather Observation Station 5
> Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.


```sql
SELECT *
FROM (
    SELECT CITY, LENGTH(CITY) AS LEN
    FROM STATION
    ORDER BY LEN, CITY
)
WHERE ROWNUM = 1
UNION
SELECT *
FROM (
    SELECT CITY, LENGTH(CITY) AS LEN
    FROM STATION
    ORDER BY LEN DESC, CITY
)
WHERE ROWNUM = 1;
```

### Weather Observation Station 6
> Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

```sql
SELECT DISTINCT(CITY)
FROM STATION
WHERE 
    CITY LIKE 'A%' OR
    CITY LIKE 'E%' OR
    CITY LIKE 'I%' OR
    CITY LIKE 'O%' OR
    CITY LIKE 'U%';
```
OR
```sql
SELECT DISTINCT(CITY)
FROM STATION
WHERE LOWER(SUBSTR(CITY, 1, 1)) in ('a','e','i','o','u');
```

### Weather Observation Station 7
> Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

```sql
SELECT DISTINCT(CITY)
FROM STATION
WHERE LOWER(SUBSTR(CITY, -1, 1)) in ('a','e','i','o','u');
```