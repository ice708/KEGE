# № 17550 Основная волна 08.06.24 (Уровень: Базовый)
# Откройте файл электронной таблицы, содержащей 
# в каждой строке шесть натуральных чисел. 
# Определите количество строк таблицы, 
# содержащих числа, для которых выполнены оба условия:
# – в строке только одно число повторяется трижды, 
# остальные числа различны; 
# – квадрат суммы всех повторяющихся чисел строки 
# больше квадрата суммы всех её неповторяющихся чисел. 
# В ответе запишите только число.

# Ответ: 19

count = 0
for line in open('c:/KEGE/09_17550.txt'):
    a = [int(x) for x in line.split()]
    # print(a)
    p3 = [x for x in a if a.count(x) == 3]
    # print(p3)
    np = [x for x in a if a.count(x) == 1]
    # print(np)
    if len(p3) == 3 and len(np) == 3:
        if sum(p3) ** 2 > sum(np) ** 2:
            count += 1
    
print(count)
