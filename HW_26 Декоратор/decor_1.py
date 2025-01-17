from string import (
    ascii_lowercase, ascii_uppercase,
    punctuation)


def register_user():




has_digit = False
has_upper = False
has_lower = False
has_symbol = False

for char in user_password:
    if ord(char) >= 48 and ord(char) <= 57:
        has_digit = True
    elif char in ascii_uppercase:
        has_upper = True
    elif char in ascii_lowercase:
        has_lower = True
    elif char in punctuation:
        has_symbol = True   

if (has_digit == True) and (has_upper == True) and (has_lower == True) and (has_symbol == True) and (len(user_password) >= 8):
    print("Успешная регистрация")
else:
    print("Ошибка")    


user_password = input("Введите пароль: ")