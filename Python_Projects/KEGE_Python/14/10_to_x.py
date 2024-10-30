# Алгоритм перевода числа из 10-ой СС в систему счисления (от 2 до 36)

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