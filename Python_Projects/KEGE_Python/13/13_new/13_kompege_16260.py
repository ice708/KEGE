# № 16260
# https://kompege.ru/task

# Известно два узла с IP-адресами 123.20.103.136 и 123.20.103.151 
# принадлежат разным сетям с одинаковой маской.
# Определите значение 4 байта маски в этих сетях. 
# Найденное значение представьте в десятичной системе счисления.

from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'123.20.103.136/{mask}', 0)
    net2 = ip_network(f'123.20.103.151/{mask}', 0)

    if net1.network_address != net2.network_address:
        print(net1.netmask)