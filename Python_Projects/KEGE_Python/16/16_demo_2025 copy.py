import sys
sys.setrecursionlimit(1000)  # Увеличение предела рекурсии

def F(n):
    if n == 1:
        return 1
    if n > 1:
        # return (F(n - 1) * 10)
        # return (1 + F(n // 2)+F(n-1))
        return (F(n-1) + 5)
result = (F(3))
print(int(result))