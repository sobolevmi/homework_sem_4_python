# Программа по формированию коэффициентов многочлена случайным образом
# и записи в файл многочлена заданной натуральной степени

from random import randint

first_monomial = str(randint(0, 100))
second_monomial = str(randint(0, 100))
third_monomial = str(randint(0, 100))

k = str(input("Введите степень многочлена: "))

user_file = open("text.txt", "w")
user_file.write(first_monomial + " " + "*" + " " + "x" + "**" + k)
user_file.write(" " + "+" + " ")
user_file.write(second_monomial + " " + "*" + " " + "x")
user_file.write(" " + "+" + " ")
user_file.write(third_monomial + " = 0")
user_file.close()

user_file = open("text.txt", "r")
print(user_file.read())
user_file.close()