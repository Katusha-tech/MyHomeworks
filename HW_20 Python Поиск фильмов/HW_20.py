import os

os.system('cls')

from pprint import pprint

from marvel import small_dict
# Задача 1
user_int = input('Введите название фильма: ')
list_user = []
for key, value in small_dict.items():
    if value is None:
        continue
    if user_int.lower() in key.lower():
        list_user.append((key, value))
if list_user:
    print('Найденные фильмы:')
    print(list_user)
else:
    print('Фильмы не найдены')

# Задача 2.1 распечатка названий фильмов после 2024
print('Фильмы, вышедшие после 2024 года: ')
for title, year in small_dict.items():
    if isinstance(year, int) and year > 2024:
        print(title)

# Задача 2.2 Список названий фильмов
movies_list = []
for title, year in small_dict.items():
    if isinstance(year, int) and year > 2024:
        movies_list.append(title)
print(movies_list)

# Задача 2.3 фильтрованный по году
filter_list = {}
for title, year in small_dict.items():
    if isinstance(year, int) and year > 2024:
        filter_list[title] = year
print(filter_list)

# Задача 2.4 список словарей в формате
list_of_dict = []
for title, year in small_dict.items():
    if isinstance(year,int) and year > 2024:
        list_of_dict.append({title: year})
print(list_of_dict)








