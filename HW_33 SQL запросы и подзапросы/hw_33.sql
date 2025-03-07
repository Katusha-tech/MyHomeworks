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

