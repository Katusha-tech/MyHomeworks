from marvel import full_dict
from typing import List, Dict, Any, Set, Optional
from pprint import pprint


# N2 Реализация ввода от пользователя, применение int к числу с помощью map
user_input = input("Введите числа через пробел: ").split()
list_user_input: List[Optional[int]] = list(map(lambda i: (int(i) if i.isdigit() else None), user_input)) #Создали список, где заменили число -числом, а не число на None 


# N3 Создали словарь с фильтрацией по Id, используя числа из списка, который получили в пункте N2
for i in list_user_input:
    if i in full_dict.keys():
        filtered_full_dict = filter(lambda id: id in list_user_input, full_dict.keys()) # Реализовали фильтрацию по id
        dict_id: Dict[Any, Dict[str, Any]] = {key: full_dict[key] for key in filtered_full_dict} # Сгенерировали новый словарь с отфильтрованными данными

pprint(dict_id)


# N4 Set comprehension с уникальными значениями "director"
director_set: Set[str] = {movie["director"] for movie in full_dict.values() if "director" in movie} #Создали set comprehension

pprint(director_set)


# N5 Создали копию исходного словаря через dict comprehension, в котором преобразовали каждое значение "year" в строку 
copy_full_dict: Dict[Any, Dict[str, Any]] = {
    key: {k: str(v) if k == "year" else v for k, v in value.items()}
    for key, value in full_dict.items()
    }  #Создали dict comprehension

pprint(copy_full_dict)


# N6 Словарь с filter, который содержит в себе фильмы, начинающиеся на букву "Ч"

filtered_movies = filter(lambda item: item[1]["title"] and item[1]["title"].startswith("Ч"), full_dict.items())
new_dict_by_letter: Dict[Any, Dict[str, Any]]= {key: value for key, value in filtered_movies}
pprint(new_dict_by_letter)

# N7 Создать отсортированный словарь с использованием lambda по параметру "producer"

dict_producer: Dict[Any, Dict[str, Any]] = {key: value for key, value in sorted(full_dict.items(), key=lambda item: item[1]["producer"])}
pprint(dict_producer)

# N8 Создать отсортированный словарь с lambda по 2-м параметрам "producer", "director"
dict_prod_and_dir: Dict[Any, Dict[str, Any]] = {key: value for key, value in sorted(full_dict.items(), key=lambda item: (item[1]["producer"], item[1]["director"]))}
pprint(dict_prod_and_dir)

# N9 Дополнительное задание: однострочник с filter и sorted
dict_sorted_filtered: Dict[Any, Dict[str, Any]] = {key: value for key, value in sorted(filter(lambda item: item[1]["producer"] is not None and item[1]["director"] is not None, full_dict.items()), key=lambda item: (item[1]["producer"], item[1]["director"]))}
pprint(dict_sorted_filtered)

# N10 Дополнительное задание: добавление аннотаций типов переменных, проверка кода с помощью mypy
