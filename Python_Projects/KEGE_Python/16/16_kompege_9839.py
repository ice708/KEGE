# № 9839 Основная волна 27.06.23
# https://kompege.ru/task

import sys
sys.setrecursionlimit(3027)  # Увеличение предела рекурсии

def F(n):
    if n < 3:
        return 3
    if n >= 3:
        return 2 * n + 5 + F(n - 2)
    
result = F(3027) - F(3023)
print(int(result))