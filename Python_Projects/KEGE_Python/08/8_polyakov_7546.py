# Поляков Задание 8. (№ 7546) (ЕГЭ-2024) 
# Определите количество 14-ричных пятизначных чисел,
# в записи которых ровно одна цифра 9 и не более трех цифр
# с числовым значением, превышающим 10.

from itertools import *

count = 0   # счетчик комбинаций
for i in product('0123456789ABCD', repeat=5): # фукция составляет 5-значные комбинации из символов
    if i[0] != '0' and i.count('9') == 1 and len([j for j in i if j in 'BCD']) <= 3: # условие для выборки значений
        count += 1 # увеличиваем счётчик, если число подходит по условию
print(count)