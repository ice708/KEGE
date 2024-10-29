# Задача 1 Сборник 20 вариантов Крылов 2024

from itertools import *

# перечисляем все маршруты из таблицы построчно
table = '14 15 17 23 25 27 32 35 41 47 51 52 53 56 65 67 71 72 74 76'

# перечислаяем все пути из графа в прямом и обратном направлении
graph = 'AB BA AE EA BE EB BC CB CD DC CF FC CG GC DE ED EF FE FG GF'

for per in permutations('ABCDEFG'): # указываем все вершины графа
    new_graph = table
    for i in range(1,8):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*per)
# в результате получим последовательность из вершин в следующем порядке по таблице 1,2,3... и т.д.