text_user = input('Введите текст: ')
num = int(input('Введите число: '))
text = text_user.lower()  # приводим текст к нижнему регистру
result_descript = ''  # переменная для расшифрования
result_script = ''  # переменная для шифрования

# шифрование
for letter in text:
    if letter == ' ':  # если в тексте есть пробел
        result_script += letter
    elif 'а' <= letter <= 'я':  # для русских букв
        scription = (ord(letter) - ord('а') + num) % 32 + ord('а')
        let_script = chr(scription)
        result_script += let_script
    elif 'a' <= letter <= 'z':  # для английских букв
        scription = (ord(letter) - ord('a') + num) % 26 + ord('a')
        let_script = chr(scription)
        result_script += let_script
    else:
        result_script += letter  # для остальных символов
print(f'Зашифрованный текст: {result_script}')

# дешифрование
for letter in text:
    if letter == ' ':  # для пробелов
        result_descript += letter
    elif 'а' <= letter <= 'я':  # для русских букв
        description = (ord(letter) - ord('а') - num) % 32 + ord('а')
        let_descript = chr(description)
        result_descript += let_descript
    elif 'a' <= letter <= 'z':  # для английских букв
        description = (ord(letter) - ord('a') - num) % 26 + ord('a')
        let_descript = chr(description)
        result_descript += let_descript
    else:
        result_descript += letter
print(f'Расшифрованный текст: {result_descript}')





