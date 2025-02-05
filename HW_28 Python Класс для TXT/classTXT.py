import os
os.system("cls") # очищение терминала


class TxtFileHandler:
    """
    Класс для работы с тексовыми файлами(чтение, запись, добаавление)
    """
    def __init__(self, filepath: str):
        """
        Инициализация класса с указанием пути к файлу.
        :param filepath: путь к файлу
        """
        self.filepath = filepath


    def read_file(self, encoding: str = "utf-8") -> str:
        """
        Чтение данных из TXT файла и возвращение в виде строки,
        eсли файл не найден, возвращает пустую строку
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        try:
            with open(self.filepath, 'r', encoding=encoding) as file:
                return file.read()
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return ""
            

    def write_file(self, *data: str, encoding: str = "utf-8") -> None:
        """
        Запись данных в TXT файл, перезаписывая его содержимое
        :param data: данные для записи в файл
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        with open(self.filepath, 'w', encoding=encoding) as file:
            file.write('\n'.join(data) + '\n')

    def append_file(self, *data: str, encoding: str = "utf-8") -> None:
        """
        Дозаписывание данных в TXT файл в конец файла
        :param data: данные для добавления
        :param encoding (str, optional): кодировка файла, по умолчанию 'utf-8'
        """
        with open(self.filepath, 'a', encoding=encoding) as file:
            file.write('\n'.join(data) + '\n')

# Тестирование 
handler = TxtFileHandler("my_file.txt")

# Запись в файл
handler.write_file("This is a test string.\n")

# Добавление в файл
handler.append_file("This is another string.\n")

# Чтение из файла
content = handler.read_file()
print(content)