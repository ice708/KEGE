R = []  # пустой список для хранения результатов работы алгоритма


def decimal_to_base(n, 13):
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(x) for x in digits[::-1])

decimal_number = int(input('Число в 10-й СС: '))    # указываем число для перевода
base = int(input('Перевести в СС с основанием: '))  # указываем основание системы счисления (2-36)

result = decimal_to_base(decimal_number, base)
print(result)

def decimal_to_base(n, base):
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(x) for x in digits[::-1])

decimal_number = int(input('Число в 10-й СС: '))    # указываем число для перевода
base = int(input('Перевести в СС с основанием: '))  # указываем основание системы счисления (2-36)

result = decimal_to_base(decimal_number, base)
print(result)

for N in range(1, 12+1):    # числа не больше 12 (перебираем числа от 1 до 12)
    N_bin = bin(N)[2:]  # переводим в 2-ую СС и удаляем префикс '0b'с помощью среза
    if N % 2 == 0:  # проверяем исходное десятичное число N на чётность
        R_bin = '10' + N_bin    # диписываем слева 01
    else:
        R_bin = '1' + N_bin + '01'  # диписываем слева 1 и справа 01
    R.append(int(R_bin, 2)) # добавляем число в список R, переводя из 2-ой СС в 10-ю СС
print(max(R))   # выводим на экран максимальное