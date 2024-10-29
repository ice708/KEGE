# https://education.yandex.ru/ege/task/8cabd46a-2193-441f-b07b-64a2bdf117a5

# Сеть задана IP-адресом 95.112.224.0 и маской сети 255.255.255.128.

# Сколько в этой сети IP-адресов, в которых правый байт адреса 
# представляет собой палиндром, то есть читается 
# слева направо и справа налево одинаково?

from ipaddress import *

net = ip_network('95.112.224.0/255.255.255.128')

k = 0
for ip in net:
    ip = str(ip)
    dot_index = ip.rfind('.')
    ip = ip[dot_index + 1 :]
    
    int_ip = int(ip)
    bin_ip = bin(int_ip)[2:]
    bin_ip_8 = bin_ip.zfill(8)

    if bin_ip_8 == bin_ip_8[::-1]:
        k += 1
print(k)

# ИЛИ

from ipaddress import ip_network

net = ip_network('95.112.224.0/255.255.255.128')
k = sum(1 for ip in net if (bin(int(str(ip).split('.')[-1]))[2:].zfill(8) == 
                            bin(int(str(ip).split('.')[-1]))[2:].zfill(8)[::-1]))
print(k)