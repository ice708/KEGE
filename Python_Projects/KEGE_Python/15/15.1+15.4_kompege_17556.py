# № 17556 Основная волна 08.06.24 (Уровень: Базовый)
# https://kompege.ru/task

def DEL(n, m):
    return n % m == 0

B = list(range(70, 91))

for A in range(1000, 0, -1):
    for x in range(1000):
        if (DEL(x, A) or ((x in B) <= (not(DEL(x ,22))))) == False:
            break
    else:
        print(A)
        break