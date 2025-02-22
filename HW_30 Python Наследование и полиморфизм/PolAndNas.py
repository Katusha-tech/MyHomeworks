import os
os.system("cls") # очищение терминала

from abc import ABC, abstractmethod

class AbstractFile(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data: list[dict]):
        pass

    @abstractmethod
    def append(self, data: list[dict]):
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
    def read(self):
        pass
    def write(self):
        pass
    def append(self):
        pass

class CsvFile(AbstractFile):
    def read(self):
        pass
    def write(self):
        pass
    def append(self):
        pass