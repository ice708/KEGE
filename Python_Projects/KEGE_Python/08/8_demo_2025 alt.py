# Альтернативный вариат решения
# ФИПИ ДЕМО 2025. Задание 8.
# Определите  количество  12-ричных  пятизначных  чисел,  в  записи  которых 
# ровно  одна  цифра  7  и  не  более  трёх  цифр  с  числовым  значением, 
# превышающим 8


k=0
for x1 in '123456789AB':
    for x2 in '0123456789AB':
        for x3 in '0123456789AB':
            for x4 in '0123456789AB':
                for x5 in '0123456789AB':
                    s=x1+x2+x3+x4+x5
                    if s.count('7') == 1 and len([j for j in s if j in '9AB']) <= 3:
                        k += 1  
print(k)