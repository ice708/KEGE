# № 17972 
# https://kompege.ru/task

# Сеть задана IP-адресом 123.222.111.192 и маской сети 255.255.255.248. 
# Сколько в этой сети IP-адресов, для которых количество нулей 
# в двоичной  записи четвертого байта IP-адреса не делится без остатка на 3?

from ipaddress import *

net = ip_network(f'123.222.111.192/255.255.255.248', 0)

count = 0
for ip in net:
    if f'{ip:b}'[24:].count('0') % 3 != 0:
        count += 1
print(count)