# Программа по вычислению числа пи с заданным количеством знаков после запятой
def pi_number():
    """Функция по вычислению числа пи"""
    res = 0
    k = pow(10, -10002)
    st16 = 1
    for i in range(0, 100):
        k1 = i
        k2 = k1 * k1
        k3 = k2 * k1
        k4 = k3 * k1

        numerator_ = (120 * k2 + 151 * k1 + 47) + k
        denominator_ = (512 * k4 + 1024 * k3 + 712 * k2 + 194 * k1 + 15) * st16
        st16 = st16 * 16
        res = (res + numerator_ / denominator_)
    return res

n = int(input("Введите требуемое число знаков после запятой числа пи: "))
p = pi_number()
new_str = (str(p).split(sep = "."))

str_left = new_str[0]
str_right = new_str[1]

result = str_left + "." + str_right[0:n]

print(result)