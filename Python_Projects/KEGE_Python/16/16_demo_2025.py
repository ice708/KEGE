import sys
sys.setrecursionlimit(1000)  # Увеличение предела рекурсии

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return ((n - 1) * F(n - 1))

result = (F(2024) + 2 * F(2023)) / F(2022)
print(int(result))