# вычисляем значение выражения
num = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2025

# Считаем количество значащих нулей

num_list = []
while num > 0:
    num_list.append(num % 25)
    num //= 25
print(num_list.count(0))

# k = 0
# while num:
#     if num % 25 == 0:
#         k += 1
#     num //= 25
# print(k)

# k = 0
# while num > 0:
#     if num % 25 == 0:
#         k += 1
#     num = num // 25
# print(k)