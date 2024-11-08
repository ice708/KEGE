# № 17635 Основная волна 19.06.24 (Уровень: Базовый)
# https://kompege.ru/task

import sys
sys.setrecursionlimit(5000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n + 1) * F(n - 1)

otvet = (F(2024) - 3 * F(2023)) / F(2022)
print(otvet)