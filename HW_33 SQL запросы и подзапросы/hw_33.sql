-- Основные задания
-- 1. Общее количество персонажей по статутусу
SELECT alive, count(*)
FROM MarvelCharacters
GROUP BY alive;

-- 2. Среднее количество появлений персонажей с разным цветом глаз
SELECT eye, AVG(appearances)
FROM MarvelCharacters
WHERE eye = 'Variable Eyes'
GROUP BY eye;

-- 3. Максимальное количество появлений у персонажей с определенным цветом волос
SELECT hair, MAX(appearances)
FROM MarvelCharacters
GROUP BY hair;

-- 4. Минимальное количество появлений среди персонажей с известной и публичной личностью
SELECT identify, MIN(appearances)
FROM MarvelCharacters
WHERE identify = 'Public Identity'
GROUP BY identify;

-- 5. Общее количество персонажей по полу
SELECT sex, count(*)
FROM MarvelCharacters
GROUP BY sex;

-- 6. Средний год первого появления персонажей с различным типом личности
SELECT Identify, AVG(year)
FROM MarvelCharacters
GROUP BY identify;

-- 7. Количество персонажей с разным цветом глаз среди живых
SELECT eye, count(*)
FROM MarvelCharacters
WHERE alive = 'Living Characters'
GROUP BY eye;

-- 8. Максимальное и минимальное количество появлений среди персонажей с определенным цветом волос
SELECT hair, MIN(appearances), MAX(appearances)
FROM MarvelCharacters
GROUP BY hair;

-- 9. Количество персонажей с различным типом личности среди умерших
SELECT identify, count(*)
FROM MarvelCharacters
WHERE alive = 'Deceased Characters'
GROUP BY identify;

-- 10. Средний год появления персонажей с различным цветом глаз
SELECT eye, AVG(year)
FROM MarvelCharacters
GROUP BY eye;

-- Подзапросы
-- 1. Персонаж с наибольшим количеством появлений 
SELECT name, appearances
FROM MarvelCharacters
ORDER BY appearances DESC
LIMIT 1;

-- 2. Персонажи, впервые появившиеся в том же году, что и персонаж с максимальными появлениями 
SELECT name, year
FROM MarvelCharacters
WHERE year = (
    SELECT year
    FROM MarvelCharacters
    ORDER BY appearances DESC
    LIMIT 1
);

-- 3. Персонажи с наименьшим количеством появлений среди живых
SELECT name, appearances
FROM MarvelCharacters
WHERE appearances = (
    SELECT MIN(appearances)
    FROM MarvelCharacters
    WHERE alive = "Living Characters"
);

-- 4. Персонажи с определенным цветом волос и максимальными появлениями среди такого цвета 
SELECT name, hair, appearances
FROM MarvelCharacters
WHERE (hair, appearances) IN (
    SELECT hair, MAX(appearances)
    FROM MarvelCharacters
    WHERE hair IS NOT NULL
    GROUP BY hair
);

-- 5. персонажи с публичной личностью и наименьшим количеством появлений
SELECT name, identify, appearances
FROM MarvelCharacters
WHERE identify='Public Identity'
AND appearances =(
    SELECT MIN(appearances)
    FROM MarvelCharacters
    WHERE identify = 'Public Identity'
);