# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=16&cat44=on&cat45=on&cat46=on&cat181=on

import sys
sys.setrecursionlimit(5000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n + 1) * F(n - 1)

otvet = (F(2024) + 3 * F(2023)) / F(2022)
print(otvet)