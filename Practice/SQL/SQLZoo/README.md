Refresh Date: 2020-08-16 

Solutions for SQLZoo 

SELECT Basics 
SELECT population FROM world WHERE name = 'Germany';
SELECT name, population FROM world WHERE name IN  ('Sweden', 'Norway', 'Denmark');
SELECT name, area FROM world WHERE area BETWEEN 200000 AND 250000;

SELECT QUIZ 
SELECT name, population FROM world WHERE population BETWEEN 1000000 and 1250000;
SELECT name FROM world WHERE name LIKE '%a' OR name LIKE '%l"; 
SELECT name, area, population FROM world WHERE area > 50000 AND population < 10000000; 
SELECT name, population/area FROM world WHERE name IN ('CHINA', 'NIGERIA', 'FRANCE', 'AUSTRALIA'); 

SELECT FROM WORLD TUTORIAL 
SELECT name, continent, population FROM world;
SELECT name FROM world WHERE population >= 200000000; 
SELECT name, gdp/population as GDP FROM world  WHERE population >= 200000000; 
SELECT name, population/1000000 FROM world WHERE continent = 'South America';
SELECT name, population FROM world where name in ('France', 'Germany', 'Italy'); 
SELECT name FROM world where name LIKE 'United%'; 
SELECT name, population, area FROM world where area >= 3000000 or population >= 250000000;
SELECT name, population, area FROM world where (area >= 3000000 xor  population < 250000000) 
SELECT name, ROUND(population/1000000, 2), ROUND(GDP/1000000000, 2) FROM world WHERE continent = 'South America'; 
SELECT name, ROUND( gdp/population, -3) FROM world where GDP >= 1000000000000; 
SELECT name, capital FROM world WHERE LENGTH(name) = LENGTH(capital); 
SELECT name, capital FROM world where LEFT(name, 1) = LEFT(capital, 1) and name <> capital; 
SELECT name FROM world WHERE name LIKE '%A%' and name LIKE '%E%' and name LIKE '%I%' and name LIKE '%O%' and name LIKE '%U%' and name not LIKE '% %'; 

SELECT from NOBEL Tutorial 