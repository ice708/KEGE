# Перевод числа из 10-ой СС в
# другую систему счисления 
# с основанием от 2 до 9

num10 = 1865   # число в 10-ой системе счисления
x = 6          # система ссчисления, в которую переводим число
numX = ''
while num10 > 0:
    numX = str(num10 % x) + numX
    num10 = num10 // x
print(numX)     # возвращается строка (str)