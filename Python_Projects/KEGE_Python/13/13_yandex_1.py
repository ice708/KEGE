# https://education.yandex.ru/ege/task/b5ea1e82-76f7-4781-8ef4-5f462fdc7638

# Два узла, находящиеся в разных подсетях,
# имеют IP-адреса 151.172.115.121 и 151.172.115.156
# В масках обеих подсетей одинаковое количество единиц.
# Укажите наименьшее возможное количество единиц в масках этих подсетей.

from ipaddress import *


def get_subnet_mask(ip):
    if ip.is_private:
        if ip in ip_network('10.0.0.0/8'):
            return '255.0.0.0'
        elif ip in ip_network('172.16.0.0/12'):
            return '255.240.0.0'
        elif ip in ip_network('192.168.0.0/16'):
            return '255.255.0.0'
    return '255.255.255.255'  # Маска по умолчанию для публичных адресов

ip1 = ip_address('151.172.115.121')
mask = get_subnet_mask(ip1)
print(f"Маска подсети для {ip1}: {mask}")

ip2 = ip_address('151.172.115.156')
mask = get_subnet_mask(ip2)
print(f"Маска подсети для {ip2}: {mask}")