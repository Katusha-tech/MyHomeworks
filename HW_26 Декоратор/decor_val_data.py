import csv

from string import (
    ascii_lowercase, ascii_uppercase,
    punctuation)

from typing import Callable

# Деократор для проверки пароля
def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1) -> Callable:
    """
    Декоратор для валидации паролей
    Параметры:
        length (int): Минимальная длина пароля (по умолчанию 8)
        uppercase (int): Минимальное количество букв верхнего регистра (по умолчанию 1)
        lowercase (int): Минимальное количество букв нижнего регистра (по умолчанию 1)
        special_chars (int): Минимальное количество спец-знаков (по умолчанию 1)
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str):
            if not password:
                raise ValueError(
                    f"Пароль не введен"
                )
            
            if len(password) < length:
                raise ValueError(
                    f"Слишком короткий пароль"
                )
            
            if sum(1 for char in password if char in ascii_uppercase) < uppercase:
                raise ValueError(
                    f"Пароль должен содержать минимум {uppercase} заглавных букв"
                )
            
            if sum(1 for char in password if char in  ascii_lowercase) < lowercase:
                raise ValueError(
                    f"Пароль должен содержать минимум {lowercase} строчных букв"
                    )
            
            if sum(1 for char in password if char in punctuation) < special_chars:
                raise ValueError(
                    f"Пароль должен содержать минимум {special_chars} специальных символов"
                    ) 
            
            return func(username, password)
        return wrapper
    return decorator


# Декоратор для проверки имени пользователя
def username_validator(func: Callable) -> Callable:
    """
    Декоратор для проверки валидации имени пользователя
    """
    def wrapper(username: str, password: str) -> str:
        if not username:
            raise ValueError (
                f"Имя пользователя не введено"
            )
        
        if " " in username:
            raise ValueError(
                f"Имя пользователь '{username}' содержит пробел."
            )
        
        return func(username, password)
    return wrapper
    

# Запись имени пользователя и пароля в CSV файл
def append_csv(username: str, password: str, file_path: str = "users.csv", delimiter=';', encoding: str ='utf-8') -> None:
    """
    Добавление данных в CSV - файл
    Args:
        username: имя пользователь
        password: пароль 
        file_path: путь к файлу
        delimiter: разделитель полей в файле (по умолчанию `';'`)
        encoding: кодировка файла
    """
    with open(file_path, "a", encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=delimiter, lineterminator="\n")
        writer.writerow([username, password])

# Функция регистрация пользователя
@password_validator(length = 8, uppercase = 1, lowercase = 1, special_chars = 1)
@username_validator
def register_user(username: str, password: str) ->str:
    append_csv(username, password)
    return "Регистрация прошла успешно!"


# Тестирование успешного случая
try:
    username = input("Введите имя пользователя: ").strip()
    password = input("Введите пароль: ").strip()
    print(register_user(username, password))
except ValueError as e:
    print(f"Ошибка: {e}")
