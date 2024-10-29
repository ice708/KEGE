# ФИПИ ДЕМО 2025. Задание 8.
# Определите  количество  12-ричных  пятизначных  чисел,  в  записи  которых 
# ровно  одна  цифра  7  и  не  более  трёх  цифр  с  числовым  значением, 
# превышающим 8

from itertools import *

count = 0
for i in product('0123456789AB', repeat=5):
    if i[0] != '0' and i.count('7') == 1 and len([j for j in i if j in '9AB']) <= 3:
        count += 1
print(count)