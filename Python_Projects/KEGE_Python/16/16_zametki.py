# Ошибка RecursionError: maximum recursion depth exceeded
import sys
print(sys.getrecursionlimit())  # показать текущий лимит рекурсии (по умолчанию 1000)
sys.setrecursionlimit(5000)     # увеличить лимит рекурсии до текущего значения

# --------------

# Ошибка OverflowError: integer division result too large for a float
from decimal import Decimal

a = Decimal('1e1000')  # Пример очень большого числа
b = Decimal('2')
result = a / b
print(result)