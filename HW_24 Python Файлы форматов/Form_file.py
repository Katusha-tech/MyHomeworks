"""
Функция JSON (чтение, запись, добавление данных)
"""
import json


"""
Функции для работы с TXT (чтение, запись, добавлени)
"""

def read_txt(file_path, encoding: str = "utf-8")->str:
    """
    Чтение текстового файла и возвращение ввиде строки
    Args:
        file_path(str): Путь к файлу для чтения
        encoding (str, optional): Кодировка файла. По умолчанию 'utf-8'
    """
    with open(file_path, 'r', encoding=encoding) as file:
        text = file.read()
    return text    


def write_txt(data, file_path, encoding: str = "utf-8") -> None:
    """
    Запись данных в текстовый файл
    Args:
        file_path(str): Путь к файлу для записи
        data: данные для записи в файл
        encoding (str, optional): кодировка файла. По умолчанию 'utf-8' 
    """
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(data + "\n")

def append_txt(data, file_path, encoding: str = "utf-8") -> None:
    """
    Добавление данных в конец текстового файла
    Args:
        data: данные для добавления в конец файла
        file_path: путь к файлу для добавления данных
        encoding (str, optional): кодировка файла. По умолчанию 'utf-8'
    """
    with open(file_path, 'a', encoding=encoding) as file:
        file.write(data)

