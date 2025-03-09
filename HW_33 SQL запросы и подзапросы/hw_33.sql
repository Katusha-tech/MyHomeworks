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

-- 3. Максимальное количесвто появлений у персонажей с определенным цветом волос
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



