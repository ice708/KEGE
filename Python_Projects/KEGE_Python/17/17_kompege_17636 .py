# № 17636
# https://kompege.ru/task

# Определите количество троек элементов последовательности, 
# в которых хотя бы один элемент оканчивается на 3 и является трёхзначным числом, 
# а сумма всех элементов меньше максимального элемента последовательности, 
# оканчивающегося на 3 и являющегося трёхзначным числом. 

# В ответе запишите количество найденных троек, затем максимальную из сумм элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.

f = [int(x) for x in open('C:/KEGE/17_17636.txt')]

max_num = 0
for i in range(len(f)):
    if (abs(i) % 10 == 3 and 100 <= abs(i) <= 999) and i > max_num:
        max_num = i

num_list = []
for i in range(len(f) - 2):
    if ((abs(f[i]) % 10 == 3 and 100 <= abs(f[i]) <= 999) 
        or (abs(f[i + 1]) % 10 == 3 and 100 <= abs(f[i + 1]) <= 999) 
        or (abs(f[i + 2]) % 10 == 3 and 100 <= abs(f[i + 2]) <= 999)):
        if (f[i] + f[i + 1] + f[i + 2]) < max_num:
            num_list.append(f[i] + f[i + 1] + f[i + 2])

print(len(num_list), max(num_list))

# РЕШЕНИЕ ЧЕРЕЗ ФУНКЦИЮ
# def usl(x):
#     return 100 <= abs(x) <= 999 and str(x)[-1] == '3'

# f = [int(x) for x in open('C:/KEGE/17_17636.txt')]
# max_num = max(x for x in f if usl(x))

# num_list = []
# for i in range(len(f) - 2):
#     if usl(f[i]) or usl(f[i + 1]) or usl(f[i + 2]):
#         if f[i] + f[i + 1] + f[i + 2] < max_num:
#             num_list.append(f[i] + f[i + 1] + f[i + 2])
# print(len(num_list), max(num_list))