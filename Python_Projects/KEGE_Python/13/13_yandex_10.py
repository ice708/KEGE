# https://education.yandex.ru/ege/task/946e0f2d-56db-4fe1-aa6a-94cd603ea823

# Сеть задана IP-адресом 195.102.65.64 и маской сети 255.255.255.192.

# Сколько в этой сети IP-адресов,
# в которых одинаковое количество нулей и единиц в правом байте адреса?

from ipaddress import *

net = ip_network('195.102.65.64/255.255.255.192', strict=True)

k=0
for ip in net:
    if bin(int(ip))[-8:].count('1') == bin(int(ip))[-8:].count('0'):
        k += 1
print(k)