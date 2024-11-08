# № 17528 Основная волна 07.06.24 (Уровень: Базовый)
# https://kompege.ru/task

# СПОСОБ 1
f_usl = 1
A = 0
otrezok = [] # необязательная переменная. искомый отрезок

for x in [k * 0.25 for k in range(-10000, 10000)]:
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    f = P <= ((Q and (not A)) <= (not P))
    if f != f_usl:
        otrezok.append(x) # все точки в искомом отрезке

print(abs(otrezok[0] - otrezok[-1])) # длина отрезка.


# СПОСОБ 2
# from itertools import *

# def f(x):
#     P = 15 <= x <= 40
#     Q = 21 <= x <= 63
#     A = a1 <= x <= a2
#     return P <= ((Q and (not A)) <= (not P))

# ox = [i / 4 for i in range(10*4, 65*4)]
# m = []

# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         m.append(a2-a1)

# print(min(m))