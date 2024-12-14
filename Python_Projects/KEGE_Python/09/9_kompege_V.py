from itertools import combinations

count = 0
for line in open('C://9.txt'):
    a = [int(x) for x in line.split()]
    n_min = min(a)
    n_max = max(a)
    n = [x for x in a if (x != n_max and x != n_min)]
    print(n)
    n.sort()
    count += 1
    if len(n) == 1:
        print(count)
        break
    found = False
#     for combo in combinations(a, 2):
#         # Вычисляем сумму первой группы
#         sum1 = sum(combo)
#         # Вычисляем сумму второй группы
#         sum2 = sum(a) - sum1
        
#         # Проверяем, равны ли суммы
#         if sum1 == sum2:
#             if (n_max - n_min) < (n[1] - n[0]):
#                 count +=1
    
# print(count)