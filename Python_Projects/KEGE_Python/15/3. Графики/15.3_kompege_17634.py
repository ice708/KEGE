# № 17634 Основная волна 19.06.24 (Уровень: Базовый)
# https://kompege.ru/task

for A in range(1000, -1, -1):
    A_is_ok = True
    for x in range(1000):
        for y in range(1000):
            if ((x + y <= 30) or (y <= x + 2) or (y >= A)) == False:
                A_is_ok = False
                break
        if A_is_ok == False:
            break    
    if A_is_ok == True:
        print(A)
        break