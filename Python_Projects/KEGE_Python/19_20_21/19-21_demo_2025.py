# Разбор
# https://www.youtube.com/watch?v=l9k6KqZ6rgw

# №19 (ответ 60)
def f(x, p):
    if x <= 19 or p > 2:
        return p == 2
    if p % 2:
        return f(x - 2, p + 1) or f(x - 5, p + 1) or f(x // 3, p + 1)
    else:
        return f(x - 2, p + 1) and f(x - 5, p + 1) and f(x // 3, p + 1)
    
print([s for s in range(100, 19, -1) if f(s, 0)])

# №20 (ответ 62, 63)
def f(x, p):
    if x <= 19 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x - 2, p + 1) or f(x - 5, p + 1) or f(x // 3, p + 1)
    else:
        return f(x - 2, p + 1) and f(x - 5, p + 1) and f(x // 3, p + 1)
    
print([s for s in range(100, 19, -1) if f(s, 0)])

# №21 (ответ 64)
def f(x, p):
    if x <= 19 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f(x - 2, p + 1) or f(x - 5, p + 1) or f(x // 3, p + 1)
    else:
        return f(x - 2, p + 1) and f(x - 5, p + 1) and f(x // 3, p + 1)
    
print([s for s in range(100, 19, -1) if f(s, 0)])