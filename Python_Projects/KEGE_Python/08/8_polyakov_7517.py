# Поляков. Задание 8. №(№ 7517) (ЕГЭ-2024)
# Все пятибуквенные слова, составленные из букв Ф, О, К, У, С 
# записаны в алфавитном порядке # и пронумерованы. 
# Вот начало списка:
# 1. ККККК
# 2. ККККО
# 3. ККККС
# 4. ККККУ
# 5. ККККФ
# ...
# Под каким номером в списке идёт последнее слово, которое 
# не содержит букв Ф и содержит ровно две буквы У?

from itertools import *

number = 0
count = 0

for i in product('КОСУФ', repeat=5):
    number += 1
    if i.count('Ф') == 0 and len([j for j in i if j in 'У']) == 2:
        count = number
print(count)