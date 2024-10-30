# https://education.yandex.ru/ege/task/11ed12f4-9275-4ed0-814c-77afcfe165c4

# Сеть задана IP-адресом 123.206.97.128 и маской сети 255.255.255.224.
# Сколько в этой сети IP-адресов, 
# оканчивающихся в двоичной записи на 101 или 010? 

from ipaddress import *

net = ip_network('123.206.97.128/255.255.255.224', strict=True)

k=0
for ip in net:
    if bin(int(ip))[-3:] == '101' or bin(int(ip))[-3:] == '010':
        k += 1
print(k)