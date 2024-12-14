# Задача 1 ФИПИ Демо 2025

from itertools import *

# перечисляем все маршруты из таблицы построчно
table = '25 20 32 18 25 10 19 13 19 22 32 13 14 20 18 10 22 14'

# перечислаяем все пути из графа в прямом и обратном направлении
graph = 'AB BF AV VA AG GA BD DB VG GV GD DG GJ JG GE EG EJ JE'

for per in permutations('ABVGDEJ'): # указываем все вершины графа
    new_graph = table
    for i in range(1,8):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*per) # *per - это распаковка элементов
                    # и передача их в качестве отдельных элементов в качестве аргуметов функции print
# в результате получим последовательность из вершин в следующем порядке по таблице 1,2,3... и т.д.