-- 1. Лысые злодеи 90-х годов (94)
SELECT name, first_appearance, appearances
FROM MarvelCharacters
WHERE hair = "Bald" and Align = "Bad Characters"
And year BETWEEN 1990 and 1999;

-- 2. Герои с тайнной идентичностью и необычными глазами (1028)
SELECT name, first_appearance, eye
FROM MarvelCharacters
WHERE identify = "Secret Identity" and eye NOT IN ('Blue Eyes', 'Brown Eyes', 'Green Eyes')
AND first_appearance NOT NULL;

-- 3. Персонажи с изменяющимся цветом волос (32)
SELECT name, hair
FROM MarvelCharacters
WHERE hair = 'Variable Hair';

-- 4. Женские персонажи с редким цветом глаз (5)
SELECT name, eye
FROM MarvelCharacters
WHERE sex = 'Female Characters' AND eye IN ('Gold Eyes','Amber Eyes');

-- 5. Персонажи без двойной идентичности и сортированные по году появления (1788)
SELECT name, first_appearance
FROM MarvelCharacters
WHERE identify = 'No Dual Identity' 
ORDER BY first_appearance DESC;

-- 6. Герои и злодеи с необычными прическами (2744)
SELECT name, align, hair
FROM MarvelCharacters
WHERE align IN ('Good Characters', 'Bad Characters') AND hair NOT IN ('Brown Hair', 'Black Hair', 'Blond Hair', 'Red Hair');

-- 7. Персонажи, появившиеся в определенное десятилетие(1306)
SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE year BETWEEN 1960 AND 1969;

-- 8. Персонажи с уникальным сочетанием цвета глаз и волос (13)
SELECT name, eye, hair
FROM MarvelCharacters
WHERE eye = 'Yellow Eyes' and hair = 'Red Hair';

--  9. Персонажи с ограниченным кооличеством появлений (11938)
SELECT name, appearances
FROM MarvelCharacters
WHERE appearances < 10;

-- 10. Персонажи с наибольшим  количеством появлений (Человек-паук, Капитан Америка, Россомаха, Железный Человек, Тор)
SELECT name, appearances
FROM MarvelCharacters
LIMIT 5;