# s - количество камней в куче
# m - количество оставшихся ходов
# h - возможные ходы

def f(s1, s2, m):
    if s1 + s2 >= 65: return m % 2 == 0 # условие победы
    if m == 0: return 0  # безуспешное завершение игры
    h = [f(s1 + 1, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1 * 3, s2, m - 1), f(s1, s2 * 3, m - 1)] # возможные ходы
    return any(h) if m % 2 != 0 else any(h) # 19 задача (неудачный первый ход)
    # return any(h) if m % 2 != 0 else all(h) # 20-21 задача

print('19', [s for s in range(1,58+1) if f(6, s, 2)])
print('20', [s for s in range(1,58+1) if not f(6, s, 1) and f(6, s, 3)])
print('21', [s for s in range(1,58+1) if not f(6, s, 2) and f(6, s, 4)])