# https://education.yandex.ru/ege/task/d3bde6f0-4eae-4994-bb5d-f757607b9d5f

# Сеть задана IP-адресом 87.226.26.72 и маской сети 255.255.255.252.
# Сколько в этой сети IP-адресов, 
# у которых количество нулей в двоичной записи IP-адреса чётно?

from ipaddress import *

# создаем сеть с IP-адресм / маской сети
net = ip_network('87.226.26.72/255.255.255.252')

k = 0 # переменная-счётчик

for ip in net: # перебираем адреса в данной сети
    # преобразуем IP в целое число и переведем в 2-ю систему счисления, 
    # найдем количество 1. Проверим НЕ кратность 5
    if bin(int(ip)).count('0') % 2 == 0: # см. файл temp.py
        k += 1  # увеличиваем счетчик при выполении условия

print(k)
