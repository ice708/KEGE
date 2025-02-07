# Задача 1 ФИПИ Демо 2025

from itertools import *

# перечисляем все маршруты из таблицы построчно
table = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'

# перечислаяем все пути из графа в прямом и обратном направлении
graph = 'AB BA AC CA AF FA BC CB CE EC DE ED DF FD DG GD EG GE '

for per in permutations('ABCDEFG'): # указываем все вершины графа
    new_graph = table
    for i in range(1,8):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*per) # *per - это распаковка элементов
                    # и передача их в качестве отдельных элементов в качестве аргуметов функции print
# в результате получим последовательность из вершин в следующем порядке по таблице 1,2,3... и т.д.