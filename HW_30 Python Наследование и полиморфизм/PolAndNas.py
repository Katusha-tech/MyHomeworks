import os
import json
import csv

os.system("cls") # очищение терминала

from abc import ABC, abstractmethod
from typing import Any

class AbstractFile(ABC):
    """
    Абстрактный класс для работы с Json-файлами, TXT-файлами и CSV-файлами
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read(self) -> Any:
        """Чтение содержимое файла"""
        pass

    @abstractmethod
    def write(self, data: Any) -> None:
        """ Записывание данных в файл """
        pass

    @abstractmethod
    def append(self, data: Any) -> None:
        """Добавление данных в файл"""
        pass

    def __str__(self):
        return f"{self.__class__.__name__} ({self.file_path})"
    

class JsonFile(AbstractFile):
    """Класс для работы с Json-файлами(чтение, запись и дозапись)"""

    def read(self, encoding: str = "utf-8"):
        """Чтение данных из Json-файла и возвращение в виде списка словарей"""
        try:
            with open(self.file_path, 'r', encoding=encoding) as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []
        
    
    def write(self, data: list[dict], encoding: str = "utf-8"):
        """
        Запись данных в Json-файл, перезаписывая его содержимое.
        :param data:данные для записи в файл
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        with open(self.file_path, 'w', encoding=encoding) as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        
    
    def append(self, data: list[dict], encoding: str = "utf-8"):
        """
        Дозапись данных в Json-файл в конец файла, если файл не найден, он будет создан.
        :param data: данные для добавления
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        # Открываем файл для чтения и получения текущих данных
        try:
            with open(self.file_path, 'r', encoding=encoding) as file:
                file_data = json.load(file)
        except FileNotFoundError:
            # Если файл не существует, создаем пустой список
            file_data = []

        if not isinstance(file_data, list):
            file_data = [file_data]
        
        # Добавляем новые данные в список
        file_data.extend(data)
        with open(self.file_path, 'w', encoding=encoding) as file:
            json.dump(file_data, file, indent=4, ensure_ascii=False)

class TxtFile(AbstractFile):
    """Класс для работы с TXT-файлами(чтение, запись, дозапись)"""

    def read(self, encoding: str = "utf-8"):
        """
        Чтение данных из TXT-файла и возвращение в виде строки, если файл не найден возвращает пустую строку.
        :param encodindg (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        try:
            with open(self.file_path, 'r', encoding=encoding) as file:
                return file.read()
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return ""


    def write(self, data:list[str], encoding: str = "utf-8"):
        """
        Запись данных в TXT-файл, перезаписывая его содержимое.
        :param data: данные для записи в файл
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        with open(self.file_path, 'w', encoding=encoding) as file:
            file.write(''.join(data))


    def append(self, data:list[str], encoding: str = "utf-8"):
        """
        Дозаписывание данных в TXT-файл в конец файла.
        :param data: данные для добавления
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        with open(self.file_path, 'a', encoding=encoding) as file:
            file.write(''.join(data))
        
class CsvFile(AbstractFile):
    """Класс для работы с CSV-файлами(чтение, запись, дозапись)"""

    def read(self, delimiter = ";",  encoding: str = "utf-8"):
        """
        Чтение данных из CSV-файла и возвращение в виде списка словарей
        :param delimiter (str, optional): разделитель полей в CSV-файле, по умолчанию ';'
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        try:
            with open(self.file_path, 'r', encoding=encoding, newline='') as file:
                reader = csv.reader(file, delimiter=delimiter)
                data = list(reader)
                return data
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []
        

    def write(self, data: list[list[str]], delimiter = ";", encoding: str = "utf-8"):
        """
        Запись данных в CSV-файл
        :param data: данные для записи в файл
        :param delimiter (str, optional): разделитель полей в CSV-файле, по умолчанию ';'
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        with open(self.file_path, 'w', encoding=encoding) as file:
            writer = csv.writer(file, delimiter=delimiter, lineterminator='\n')
            writer.writerows(data)


    def append(self, data: list[str], delimiter = ";", encoding: str = "utf-8"):
        """
        Добавление данных в CSV-файл в конец файла
        :param data: данные для добавления
        :param delimiter (str, optional): разделитель полей в CSV-файле, по умолчанию ';'
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        with open(self.file_path, 'a', encoding=encoding, newline='') as file:
            writer = csv.writer(file, delimiter=delimiter, lineterminator='\n')
            if isinstance(data[0], list): # если data - это список списков
                writer.writerows(data) # добавление строк
            else:
                writer.writerow(data) # добавление строки 
    