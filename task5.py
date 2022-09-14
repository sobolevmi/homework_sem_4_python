# Программа по записи в новый файл суммы многочленов, записанных в другие файлы
def numbers(user_string):
    """Функция по вычленению чисел из многочлена
    Авгумент user_string - строка, в которой содержится запись многочлена"""
    user_list = list()
    for i in user_string.split():
        try:
            user_list.append(int(i))
        except ValueError:
            pass
    return user_list

f1 = open("task5_file1.txt", "w")
polynomial_1 = "34 * x**2 + 21 * x + 8"
f1.write(polynomial_1)
polynomial_1_numbers = numbers(polynomial_1)
f1.close()

f2 = open("task5_file2.txt", "w")
polynomial_2 = "16 * x**2 + 29 * x + 42"
f2.write(polynomial_2)
polynomial_2_numbers = numbers(polynomial_2)
f2.close()

result_list = list()

for index in range(0, 3):
    result_list.append(polynomial_1_numbers[index] + polynomial_2_numbers[index])

polynomial_3 = str(str(result_list[0]) + " * x**2 + " + str(result_list[1]) +
                " * x + " + str(result_list[2]))

f3 = open("task5_file3.txt", "w")
f3.write(polynomial_3)
f3.close()