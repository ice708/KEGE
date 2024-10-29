# if bin(int(ip)).count('1') % 5 != 0: 
import ipaddress

ip_str = '172.16.168.0'
print('ip: ', ip_str)

ip = ipaddress.ip_address(ip_str)
int_ip = int(ip)
print('int_ip: ', int_ip)

bin_ip = bin(int_ip)
print('bin_ip: ', bin_ip)

num = bin_ip.count('1')
print(num)

# ===================
# Все IP адреса сети

# from ipaddress import *

# # создаем сеть с IP-адресм / маской сети
# net = ip_network('172.16.168.0/255.255.248.0')

# # показать все IP адреса:
# n = 0
# for ip in net:
#     print(ip)
#     n += 1
# print(n)