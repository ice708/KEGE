# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=9
# Дана программа для исполнителя Редактор:
# НАЧАЛО
# ПОКА нашлось(25) ИЛИ нашлось(35) ИЛИ нашлось(555)
#   ЕСЛИ нашлось(25)
#     ТО заменить(25, 53)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось(35)
#     ТО заменить(35, 2)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось(555)
#     ТО заменить(555, 23)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
# На вход приведённой выше программе поступает строка, начинающаяся с цифры 2, 
# а затем n подряд идущих цифр 5 (n > 3). 
# Определите наименьшее значение n, при котором сумма числовых значений цифр строки, 
# получившейся в результате выполнения программы, кратна 7.

for n in range(4, 10000):
    text = '2' + '5' * n
    print(text)
    while ('25' in text) or ('35' in text) or ('555' in text):
        if '25' in text:
            text = text.replace('25', '53', 1)
        if '35' in text:
            text = text.replace('35', '2', 1)
        if '555' in text:
            text = text.replace('555', '23', 1)
    print(text)
    if sum(int(digit) for digit in text) % 7 == 0:
        print(n)
        break
    
# ИЛИ
    # sum_digit = 0
    
    # for i in text:
    #     sum_digit = sum_digit + int(i)
    # print(sum_digit)

    # if sum_digit % 7 == 0:
    #     print(n)
    #     break