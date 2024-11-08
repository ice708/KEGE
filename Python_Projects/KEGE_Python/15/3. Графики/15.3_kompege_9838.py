# № 9838 Основная волна 27.06.23 (Уровень: Базовый)
# https://kompege.ru/task

for A in range(1000, -1, -1):
    A_is_ok = True
    for x in range(1000):
        for y in range(1000):
            if ((x + 2 * y > A) or (y < x) or (x < 30)) == False:
                A_is_ok = False
                break
        if A_is_ok == False:
            break
    else:
        print(A)
        break