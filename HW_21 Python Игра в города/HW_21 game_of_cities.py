from cities import cities_list

name_of_city = set()  # множество с городами
used_name_of_city = []  # список с использованными городами
score_user = 0  # счет пользователя
score_comp = 0  # счет компьютера
last_letter = ''
mistakes = 0  # ошибки


# достаем из словаря города и заносим во множество
for city in cities_list:
    name_of_city.add(city['name'])
# print(name_of_city)

# цикл игры
while True:
    # ход пользователя
    user_word = input("Введите город или 'стоп' для завершения игры: ").capitalize()

    if user_word == "Стоп":
        print('Игра окончена')
        break

    if user_word not in name_of_city:
        print('Такого города  нет. Попробуйте снова')
        mistakes += 1
    elif user_word in used_name_of_city:
        print('Этот город был уже использован. Подумай ещё')
        mistakes += 1
    elif last_letter and not user_word.startswith(last_letter.upper()):
        print(f'Город должен начинаться на букву "{last_letter.upper()}" Пробуй ещё')
        mistakes += 1
    else:
        mistakes = 0  # если ввод правильный, то сбросить ошибки

        # работаем со словом пользователя
        used_name_of_city.append(user_word)  # добавляем в использованные города
        name_of_city.remove(user_word)  # удаляем из основного множества
        score_user += 1

        # определяем последнюю букву города
        last_letter = user_word[-1].lower()
        if last_letter in "ьъы":
            last_letter = user_word[-2].lower()

        # ход компьютера
        next_city = None
        for city in name_of_city:
            if city.lower().startswith(last_letter) and city not in used_name_of_city:
                next_city = city
                break

        if next_city:
            print(f'Компьютер выбрал город: {next_city}')
            used_name_of_city.append(next_city)
            name_of_city.remove(next_city)  # удаляем названный город компьютером из множества
            score_comp += 1

            # определяем последнюю букву названого города компьютером
            last_letter = next_city[-1].lower()
            if last_letter in "ьъы":
                last_letter = next_city[-2].lower()
        else:
            print(f'Компьютер не смог назвать город и проиграл.')
            break

    # если есть 3 ошибки:
    if mistakes == 3:
        if score_user > score_comp:
            print(f'Ты выиграл со счетом  {score_user} - {score_comp}. Молодец!')
        elif score_comp > score_user:
            print(f'Победил компьютер со счетом  {score_comp} - {score_user}.')
        else:
            print(f'Ничья! Счет {score_user} - {score_comp}.')
        break

# результат игры
if mistakes < 3:
    if score_user > score_comp:
        print(f'Ты выиграл со счетом  {score_user} - {score_comp}. Молодец!')
    elif score_comp > score_user:
        print(f'Победил компьютер со счетом  {score_comp} - {score_user}.')
    else:
        print(f'Ничья! Счет {score_user} - {score_comp}.')








