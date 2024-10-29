# Задача 1 ФИПИ Демо 2025

from itertools import *

# перечисляем все маршруты из таблицы построчно
table = '14 15 17 24 26 35 36 37 41 42 51 53 56 62 63 65 71 73'

# перечислаяем все пути из графа в прямом и обратном направлении
graph = 'AB BA AC CA BD DB CE EC CG GC DF FD DG GD EF FE FG GF'

for per in permutations('ABCDEFG'): # указываем все вершины графа
    new_graph = table
    for i in range(1,8):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*per) # *per - это распаковка элементов
                    # и передача их в качестве отдельных элементов в качестве аргуметов функции print
# в результате получим последовательность из вершин в следующем порядке по таблице 1,2,3... и т.д.