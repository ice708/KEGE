# https://education.yandex.ru/ege/task/b5ea1e82-76f7-4781-8ef4-5f462fdc7638

# Два узла, находящиеся в разных подсетях,
# имеют IP-адреса 151.172.115.121 и 151.172.115.156
# В масках обеих подсетей одинаковое количество единиц.
# Укажите наименьшее возможное количество единиц в масках этих подсетей.

def ip_to_binary(ip):
    return ''.join(format(int(i), '08b') for i in ip.split('.'))

def find_mask(ip1, ip2):
    binary_ip1 = ip_to_binary(ip1)
    binary_ip2 = ip_to_binary(ip2)

    for mask in range(32):
        binary_mask = '1' * mask + '0' * (32 - mask)
        if (int(binary_ip1, 2) & int(binary_mask, 2)) != (int(binary_ip2, 2) & int(binary_mask, 2)):
            return '.'.join(str(int(binary_mask[i:i+8], 2)) for i in range(0, 32, 8))

def mask_to_binary(mask):
    binary_mask = ''
    for octet in mask.split('.'):
        binary_octet = format(int(octet), '08b')
        binary_mask += binary_octet
    formatted_binary_mask = '.'.join([binary_mask[i:i+8] for i in range(0, 32, 8)])
    return formatted_binary_mask, binary_mask.count('1')

ip1 = '151.172.115.121'
ip2 = '151.172.115.156'

mask = find_mask(ip1, ip2)
binary_mask, ones_count = mask_to_binary(mask)

print(f'Маска сети: {mask}')
print(f'Бинарная маска: {binary_mask}')
print(f'Количество единиц: {ones_count}')