# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=16&cat44=on&cat45=on&cat46=on&cat181=on

import sys
sys.setrecursionlimit(5000)

def F(n):
    if n <= 2025:
        return(1)
    if n > 2025:
        return F((n + 2024) // 2025) + 1

n = 0
for i in range(1, 2026):
    n += i ** i

print(F(n))