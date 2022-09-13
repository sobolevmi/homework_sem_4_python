# Программа по выведению списка всех простых множителей числа
def factoring(user_number):
    """Функция по разложению числа на простые множители.
    Аргумент user_number - введенное пользователем с клавиатуры число"""
    fact = list()
    for i in range(2, user_number + 1):
        while user_number % i == 0:
            fact.append(i)
            user_number = user_number / i
    return fact

number = int(input("Введите число: "))
print(factoring(number))