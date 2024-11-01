# № 18159
# https://kompege.ru/task

# Для узла с IP-адресом 205.154.212.20 адрес сети равен 205.154.192.0. 
# Чему равно наибольшее возможное значение третьего слева байта маски? 

from ipaddress import *

ip = IPv4Address('205.154.212.20')

for mask in range(32, 0, -1):
    net = ip_network(f'205.154.192.0/{mask}', 0)

    for host in net.hosts():
        if ip == host:
            print(net.netmask)