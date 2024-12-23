# https://education.yandex.ru/ege/task/efa830d3-9d5f-40b1-8630-3c767db89078

# Два узла, находящиеся в одной сети, имеют IP-адреса 121.171.5.70 и 121.171.5.107. 
# Укажите наименьшее возможное количество адресов в этой сети.

# РЕШЕНИЕ:
# Т.к. начало адресов совпадает,
# то найдем разницу последних октетов (последние 8 бит)
# 107 - 70 = 37

# Чтобы определить, сколько адресов нужно,
# нужно найти ближайшую степень двойки, 
# которая больше или равна 38
# (так как 37 адресов + 1 для сети).
# Наименьшая степень двойки, 
# которая больше или равна 38, это 64 (2^6).

# Следовательно, наименьшее возможное количество адресов в этой сети:
# 64 адреса.

# ----  ИЛИ  ----

# По Таблице соответствия масок подсетей:
#      Маска            | Доступные адреса
# 255.255.255.192 /26             64
# 255.255.255.224 /27             32

# 32 < 37 < 64
# Следовательно, чтобы адреса были в одной подсети 
# нужна маска /26. При этом доступно 64 адресов.
# Ответ: 64


ip1 = '121.171.5.70'
ip2 = '121.171.5.107'

# n = (abs((int(bin(int(ip1))[-8:], base = 2)) - (int(bin(int(ip2))[-8:], base = 2)))) + 1

# 2-ой способ 

# dot_index1 = ip1.rfind('.')
# ip1 = ip1[dot_index1 + 1 :]

# dot_index2 = ip2.rfind('.')
# ip2 = ip2[dot_index2 + 1 :]

# ---- каскадное присвоение ----

dot_index1, dot_index2 = ip1.rfind('.'), ip2.rfind('.')
ip1, ip2 = ip1[dot_index1 + 1 :], ip2[dot_index2 + 1 :]

n = abs(int(ip1) - int(ip2)) + 1

for i in range(8):
    if 2 ** i >= n:
        print(2**i)
        break