# https://education.yandex.ru/ege/task/72700a25-e574-40cb-b177-c612540ea5b4
# ФИПИ

# На вход приведённой выше программе поступает строка, начинающаяся с цифры «2», а затем содержащая n цифр «5» (n > 3).
# Определите наименьшее значение n, при котором сумма цифр в строке, получившейся в результате выполнения программы, равна 17.

# НАЧАЛО
# ПОКА нашлось (25) ИЛИ нашлось (355) ИЛИ нашлось (555)
#     ЕСЛИ нашлось (25)
#         ТО заменить (25, 5)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (355)
#         ТО заменить (355, 52)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (555)
#         ТО заменить (555, 3)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ

for n in range(4, 10000):
    text = '2' + '5' * n
    
    while '25' in text or '355' in text or '555' in text:
        if '25' in text:
            text = text.replace('25', '5', 1)
        if '355' in text:
            text = text.replace('355', '52', 1)
        if '555' in text:
            text = text.replace('555', '3', 1)
    
    if sum(int(digit) for digit in text) == 17:
        print(n)
        break
    
# ИЛИ
    # sum_digit = 0
    
    # for i in text:
    #     sum_digit += int(i)
    # print(sum_digit)

    # if sum_digit == 17:
    #     print(n)
    #     break