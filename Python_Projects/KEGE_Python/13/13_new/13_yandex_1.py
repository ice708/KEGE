# https://education.yandex.ru/ege/task/b5ea1e82-76f7-4781-8ef4-5f462fdc7638

# Два узла, находящиеся в разных подсетях,
# имеют IP-адреса 151.172.115.121 и 151.172.115.156
# В масках обеих подсетей одинаковое количество единиц.
# Укажите наименьшее возможное количество единиц в масках этих подсетей.

from ipaddress import *

host1 = '151.172.115.121'
host2 = '151.172.115.156'

for mask in range(33):
    sub_net1 = ip_network(f'{host1}/{mask}', 0)
    sub_net2 = ip_network(f'{host2}/{mask}', 0)

    if sub_net1 != sub_net2:
        print(mask)
        break

