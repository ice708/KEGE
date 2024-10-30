# https://education.yandex.ru/ege/task/812a3ebe-1858-4d22-8bfc-9c4509599174

# ФИПИ
# Сеть задана IP-адресом 192.168.32.160 и маской сети 255.255.255.240.

# Сколько в этой сети IP-адресов, 
# для которых сумма единиц в двоичной записи IP-адреса чётна?

from ipaddress import *

net = ip_network('192.168.32.160/255.255.255.240', strict=True)

k=0
for ip in net:
    if bin(int(ip)).count('1') % 2 == 0:
        k += 1
print(k)