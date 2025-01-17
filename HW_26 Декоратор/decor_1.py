from string import (
    ascii_lowercase, ascii_uppercase,
    punctuation, digits)


def register_user(user_password:str = ""):
    """
    Функция, которая проверяет вводимый пароль на определенные критерии
    :param user_password: str - пароль, который вводит пользователь
    """
    if not user_password:
        return "Пароль не введен"
    
    if len(user_password) < 8:
        return "Слишком короткий пароль"

    has_digit = False
    has_upper = False
    has_lower = False
    has_symbol = False

    for char in user_password:
        if char.isdigit():
            has_digit = True
        elif char in ascii_uppercase:
            has_upper = True
        elif char in ascii_lowercase:
            has_lower = True
        elif char in punctuation:
            has_symbol = True

    if not has_digit:
        return "Пароль должен содержать цифры"
    if not has_upper:
        return "Пароль должен содержать заглавную букву"
    if not has_lower:
        return "Пароль должен содержать строчную букву"
    if not has_symbol:
        return "Пароль должен содержать символы"
    
    return "Успешная регистрация"


user_password = input("Введите пароль: ")
result = register_user(user_password)
print(result)