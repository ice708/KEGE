import ipaddress

# IP-адреса
ip1 = "121.171.5.70"
ip2 = "121.171.5.107"

# Преобразуем IP-адреса в объекты IP
ip_obj1 = ipaddress.ip_address(ip1)
ip_obj2 = ipaddress.ip_address(ip2)

# Находим общую сеть, включающую оба IP
for mask_length in range(32, -1, -1):
    net = ipaddress.ip_network(f"{ip1}/{mask_length}", strict=False)
    if ip_obj2 in net:
        network = net
        break

# Количество адресов в сети
num_addresses = network.num_addresses
print("Наименьшее возможное количество адресов в этой сети:", num_addresses)