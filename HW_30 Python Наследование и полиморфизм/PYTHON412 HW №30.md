---
project: "[[Академия TOP]]"
journal: "[[PYTHON412]]"
tags:
  - PYTHON412
date: 2025-01-28
type:
  - home work
hw_num: 30
topic: "В данном задании вам предстоит создать классы для работы с различными типами файлов: JSON, TXT и CSV. Вы также создадите абстрактный класс, который будет предписывать методы для чтения, записи и добавления данных в файлы. Ваша задача — реализовать наследование и полиморфизм в Python с использованием библиотеки ABC."
hw_theme:
  - txt
  - ООП
  - python
  - Наследование
  - ABC
  - "@abstractmethod"
  - JSON
  - CSV
st_group: python 412
links:
---
# Домашнее задание 📃

## Краткое содержание

В данном задании вам предстоит создать классы для работы с различными типами файлов: JSON, TXT и CSV. Вы также создадите абстрактный класс, который будет предписывать методы для чтения, записи и добавления данных в файлы. Ваша задача — реализовать наследование и полиморфизм в Python с использованием библиотеки ABC.

### Технологии: 🦾
- Python
- Модуль `abc` для создания абстрактных классов
- Работа с файлами JSON, TXT, CSV

## Задание 👷‍♂️

Создайте модуль `file_classes.py`, содержащий следующие классы:

### Абстрактный класс и его наследники

1. **Класс `AbstractFile`**
   - Родитель: `ABC`
   - Методы:
     - `read()`: Абстрактный метод для чтения данных из файла.
     - `write(data)`: Абстрактный метод для записи данных в файл.
     - `append(data)`: Абстрактный метод для добавления данных в файл.

2. **Класс `JsonFile`**
   - Родитель: `AbstractFile`
   - Атрибуты:
     - `file_path`: Путь к файлу.
   - Методы:
     - Реализовать методы `read`, `write` и `append` для работы с JSON-файлами.

3. **Класс `TxtFile`**
   - Родитель: `AbstractFile`
   - Атрибуты:
     - `file_path`: Путь к файлу.
   - Методы:
     - Реализовать методы `read`, `write` и `append` для работы с текстовыми файлами.

4. **Класс `CsvFile`**
   - Родитель: `AbstractFile`
   - Атрибуты:
     - `file_path`: Путь к файлу.
   - Методы:
     - Реализовать методы `read`, `write` и `append` для работы с CSV-файлами.

### Вызов методов

Создайте модуль `file_tests.py`, в котором вы протестируете все созданные классы. Вызовите методы `read`, `write` и `append` для каждого типа файла с использованием конструкции `if __name__ == "__main__":`.

### Таблица классов и методов

| Класс    | Родитель     | Методы                           |
| -------- | ------------ | -------------------------------- |
| `JsonFile` | `AbstractFile` | `read()`, `write(data)`, `append(data)` |
| `TxtFile` | `AbstractFile` | `read()`, `write(data)`, `append(data)` |
| `CsvFile` | `AbstractFile` | `read()`, `write(data)`, `append(data)` |

>[!warning]
>### Критерии проверки 👌
>- Соблюдение принципов ООП (наследование, полиморфизм).
>- Корректная реализация абстрактных методов в наследниках.
>- Реализация и тестирование всех методов `read`, `write`, `append` для каждого типа файла.
>- Код должен быть оформлен в соответствии с PEP-8.
>- Не менее **5 коммитов** в репозитории GitHub.
>- Архив с домашним заданием должен содержать текстовый документ с ссылкой на репозиторий GitHub.
>- Документация для всех классов и методов, включая аннотации типов.


