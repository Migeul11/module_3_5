# Пункты задачи:
#
# 1. Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):

    # 2. Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    str_number = str(number)

    # 3. Основной задачей будет отделение первой цифры в числе: создайте переменную first
    # и запишите в неё первый символ из str_number в числовом представлении(int).
    first = int(str_number[0])

    # 4. Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
    # Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
    # 5. 4 пункт можно выполнить только тогда, когда длина str_number больше 1,
    # т.к. в противном случае не получиться взять срез str_number[1:].
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))

    # 6. Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
    return first


result = get_multiplied_digits(40203)
print(result)
