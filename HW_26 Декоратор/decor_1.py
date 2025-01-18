from string import (
    ascii_lowercase, ascii_uppercase,
    punctuation)
from typing import Callable

def password_checker(func: Callable) -> Callable:
    def wrapper(user_password: str):
        """
        Обертка для функции, проверяющая пароль перед выполнением основной логики
        """
        if not user_password:
            return "Пароль не введен"
    
        if len(user_password) < 8:
            return "Слишком короткий пароль"

        has_digit = any(char.isdigit() for char in user_password)
        has_upper = any(char in ascii_uppercase for char in user_password)
        has_lower = any(char in ascii_lowercase for char in user_password)
        has_symbol = any(char in punctuation for char in user_password)

        if not has_digit:
            return "Пароль должен содержать цифры"
        if not has_upper:
            return "Пароль должен содержать заглавную букву"
        if not has_lower:
            return "Пароль должен содержать строчную букву"
        if not has_symbol:
            return "Пароль должен содержать символы"
        
        return func(user_password)
    return wrapper

@password_checker
def register_user(user_password: str):
    return "Успешная регистрация"
    

user_password = input("Введите пароль: ")
result = register_user(user_password)
print(result)


