# Программа по выводу списка неповторяющихся элементов исходной последовательности

def fill_list_from_user():
    """ Функция по заполнению созданного списка вручную пользователем"""
    size = int(input("Введите размер создаваемого списка: "))
    any_list = list()
    for i in range(size):
        any_list.append(int(input("Введите элемент списка: ")))
    return any_list

def fill_list_from_random():
    """ Функция по заполнению созданного списка случайно сгенерированными числами"""
    import random
    length = int(input("Введите размер списка: "))
    start = int(input("Введите начало диапазона случайно генерируемых чисел: "))
    end = int(input("Введите конец диапазона случайно генерируемых чисел: "))
    random_list = [random.randint(start, end + 1) for i in range(length)]
    return random_list

def unique_elements(array):
    """Функция по определению неповторяющихся элементов в списке.
    Аргумент array - список пользователя"""
    unique_list = list()
    for i in range(len(array)):
        count = 0
        for j in range(0, len(array)):
            if array[i] == array[j]:
                count += 1
        if count <= 1:
            unique_list.append(array[i])
    return unique_list

user_choice = int(input("Если вы хотите заполнить список самостоятельно, нажмите 1\nЕсли вы хотите, чтобы список был заполнен"
"случайно сгенерированными числами, нажмите 2:\n"))

user_list = list()

if user_choice == 1:
    user_list = fill_list_from_user()
    print(f"{user_list} -> {unique_elements(user_list)}")
elif user_choice == 2:
    user_list = fill_list_from_random()
    print(f"{user_list} -> {unique_elements(user_list)}")
else:
    print("Вы ввели неверное число, попробуйте снова")