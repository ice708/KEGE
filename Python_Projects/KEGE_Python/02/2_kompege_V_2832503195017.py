# №2 ФИПИ Демо 2024

print('x y z w') # заголовки для колонок со значениями

# перебираем возможные варианты для каждой переменной
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (not(y <= (x == w)) and (z <= x)) == 1: # переписываем эту строку в соотвествии с данным в задаче выражением
                    print(x, y, z, w) # выводим значение переменных, комбинация которых удовлетворяет условию