import yaml
import csv
import os
import json
os.system("cls")
"""
Функция JSON (чтение, запись, добавление данных)
"""
def read_json(file_path: str, encoding: str = "utf-8"):
    """
    Чтение данных из JSON-файла
    Args:
        file_path: путь к файлу.
        encoding: кодировка файла (по умолчанию `"utf-8"`)
    """
    with open(file_path, "r", encoding = encoding) as file:
        data = json.load(file)
    return data     

def write_json(data, file_path: str, encoding: str = "utf-8"):
    """
    Запись данных в JSON-файл
    Args:
        data: данные для записи.
        file_path: путь к файлу.
        encoding: кодировка файла (по умолчанию `"utf-8"`)
    """
    with open(file_path, "w", encoding = encoding) as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)


def append_json(data: list[dict], file_path: str, encoding: str = "utf-8"):
    """
    Добавление данных в существующий JSON-файл
    Args:
        data: список словарей с данными для добавления.
        file_path: путь к файлу.
        encoding: кодировка файла (по умолчанию `"utf-8"`)
    """
    if os.path.exists(file_path): #Если файл существует, читаем данные или создаем пустой список
        with open(data, file_path, "r", encoding=encoding) as file:
            data = json.load(file)
    else:
        data = []

    data.extend(data) #Добавляем новые данные

    with open(file_path, 'w',encoding=encoding) as file: #Записываем обновленные данные в файл
        json.dump(data, file_path, indent = 4, ensure_ascii= False)    


"""
Функции для работы с CSV
"""
def read_csv(file_path, delimiter=';', encoding: str ='utf-8'):
    """
    Чтение данных из CSV-файла
    Args:
        file_path: путь к файлу
        delimiter: разделитель полей в файле (по умолчанию `';'`)
        encoding: кодировка файла
    """
    with open(file_path, "r", encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        data = list(reader)
    
    return data


def write_csv(data, file_path, delimiter=';', encoding: str = 'utf-8') -> None:
    """
    Запись данных в CSV-файл
    Args:
        data: данные для записи
        file_path: путь к файлу
        delimiter: разделитель полей в файле (по умолчанию `';'`)
        encoding: кодировка файла 
    """
    with open(file_path, "w", encoding="utf-8-sig", newline='') as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator="\n")
        writer.writerows(data)


def append_csv(data, file_path, delimiter=';', encoding: str ='utf-8') -> None:
    """
    Добавление данных в CSV - файл
    Args:
        data: данные для добавления
        file_path: путь к файлу
        delimiter: разделитель полей в файле (по умолчанию `';'`)
        encoding: кодировка файла
    """
    with open(file_path, "a", encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator="\n")
        if isinstance(data[0], list): #если data - это список списков
            writer.writerows(data) #добавление строк
        else:    
            writer.writerow(data) #добавление строки

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
        file.write(data + '\n')

"""
Функция для работы с YAML
"""
def read_yaml(file_path):
    """
    Чтение данных из YAML-файла
    Args:
        file_path: путь к файлу
    """
    with open (file_path, "r", encoding = "utf-8") as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data


