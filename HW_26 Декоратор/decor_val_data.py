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
        def wrapper(user_password: str):
            if not user_password:
                return "Пароль не введен"
    
            if len(user_password) < length:
                return "Слишком короткий пароль"
            
            if sum(1 for char in  user_password if char in ascii_uppercase) < uppercase:
                return f"Пароль должен содержать минимум {uppercase} заглавных букв"
            
            if sum(1 for char in  user_password if char in  ascii_lowercase) < lowercase:
                return f"Пароль должен содержать минимум {lowercase} строчных букв"
            
            if sum(1 for char in user_password if char in punctuation) < special_chars:
                return f"Пароль должен содержать минимум {special_chars} специальных символов"
            
            return func(user_password)
        
        return wrapper
    
    return decorator


@password_validator(length = 8, uppercase = 1, lowercase = 1, special_chars = 1)
def register_user(user_password: str) ->str:
    return "Успешная регистрация"


# Декоратор для проверки имени пользователя
def username_validator(func: Callable) -> Callable:
    """
    Декоратор для проверки валидации имени пользователя
    """
    def wrapper(user_name:str) -> str:
        if not user_name:
            return "Имя пользователя не введено"
        
        if " " in user_name:
            raise ValueError(
                f"Имя пользователь '{user_name}' содержит пробел."
            )
        
        return func(user_name)
    
    return wrapper
    
@username_validator
def register_user_name(user_name: str) -> str:
    return "Имя введено верно"


# Ввод пользователя
user_password = input("Введите пароль: ")
print(register_user(user_password))

user_name = input("Введите имя пользователя: ").strip()
try:
    print(register_user_name(user_name))
except ValueError as e:
    print(f"Ошибка: {e}")
