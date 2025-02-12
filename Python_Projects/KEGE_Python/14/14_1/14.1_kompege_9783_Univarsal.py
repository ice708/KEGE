# № 9783 Основная волна 20.06.23 (Уровень: Базовый)
# https://kompege.ru/task
# Операнды арифметического выражения записаны в системе счисления с основанием 22.
# 18x89957(22)+80x33(22)+521x6(22)
# В записи чисел переменной x обозначена неизвестная цифра из 
# алфавита 22-ричной системы счисления. 
# Определите наименьшее значение x, при котором значение данного арифметического 
# выражения кратно 21. Для найденного значения x вычислите частное от 
# деления значения арифметического выражения на 21 и 
# укажите его в ответе в десятичной системе счисления. 
# Основание системы счисления указывать не нужно.

num1 = '18x89957'    # первое число
num2 = '80x33'      # второе число
num3 = '521x6'       # третье число
ss = 22             # cистема счисления (СС)

for x in range(ss):
    n1 = 0
    n2 = 0
    n3 = 0

    # Первое число в 10-ой СС
    for i in range(len(num1)):
        if num1[i] != 'x':
            n3 += int(num1[i]) * ss ** (len(num1) - i - 1)
        else:
            n3 += x * ss ** (len(num1)- i - 1 )

    # Второе число в 10-ой СС
    for i in range(len(num2)):
        if num2[i] != 'x':
            n3 += int(num2[i]) * ss ** (len(num2)- i - 1)
        else:
            n3 += x * ss ** (len(num2) - i - 1)

    # Третье число в 10-ой СС
    for i in range(len(num3)):
        if num3[i] != 'x':
            n3 += int(num3[i]) * ss ** (len(num3)- i - 1)
        else:
            n3 += x * ss ** (len(num3) - i - 1)

    znachenie = n1 + n2 + n3    # выражение, которое дано по условию задачи
    if znachenie % 21 == 0:     # ОСНОВНОЙ ВОПРОС ЗАДАЧИ
         print(znachenie // 21)
         break