name_student = input('Введите имя студента: ')
mark = input('Введите оценку: ')

if mark.isdigit():
    mark_of_student = int(mark)
    if 1 <= mark_of_student <= 3:
        print(f'Имя студента: {name_student}. Уровень: начальный.')
    elif 4 <= mark_of_student <= 6:
        print(f'Имя студента: {name_student}. Уровень: средний.')
    elif 7 <= mark_of_student <= 9:
        print(f'Имя студента: {name_student}. Уровень: высокий.')
    elif 10 <= mark_of_student <= 12:
        print(f'Имя студента: {name_student}. Уровень: достаточный.')
    else:
        print("Введено некорректное значение. Пожалуйста, введите число.")

else:
    print("Введено некорректное значение. Пожалуйста, введите число.")



