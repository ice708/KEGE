# № 17679 Пересдача 04.07.24 (Уровень: Базовый)
# https://kompege.ru/task

from decimal import Decimal     # для работы с большими числами
import sys
sys.setrecursionlimit(3000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * F(n - 1)

otvet = ((F(2024)) / 7 - (F(2023))) / (F(2022))
# otvet = (Decimal(F(2024)) / 7 - Decimal(F(2023))) / Decimal(F(2022))
# otvet = ((F(2024)) // 7 - (F(2023))) // (F(2022))

print(otvet)