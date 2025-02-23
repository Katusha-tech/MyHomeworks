import os
os.system("cls") # очищение терминала

from abc import ABC, abstractmethod

class AbstractFile(ABC):
    """
    Абстрактный класс для работы с Json-файлами, TXT-файлами и CSV-файлами
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read(self) -> str:
        """Чтение содержимое файла"""
        pass

    @abstractmethod
    def write(self, data: list[dict]):
        """ Записывание данных в файл """
        pass

    @abstractmethod
    def append(self, data: list[dict]):
        """Добавление данных в файл"""
        pass

    def __str__(self):
        return f"{self.__class__.__name__} {self.file_path}"
    

class JsonFile(AbstractFile):
    def read(self):
        pass
    def write(self):
        pass
    def append(self):
        pass

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


    def write(self, *data:str, encoding: str = "utf-8"):
        """
        Запись данных в TXT-файл, перезаписывая его содержимое.
        :param data: данные для записи в файл
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        with open(self.file_path, 'w', encoding=encoding) as file:
            file.write('\n'.join(data) + '\n')


    def append(self, *data:str, encoding: str = "utf-8"):
        """
        Дозаписывание данных в TXT-файл в конец файла.
        :param data: данные для добавления
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        with open(self.file_path, 'a', encoding=encoding) as file:
            file.write('\n'.join(data) + '\n')
        
class CsvFile(AbstractFile):
    def read(self):
        pass
    def write(self):
        pass
    def append(self):
        pass