num = int(input('Число в 10-й СС: '))

b_num = bin(num)[2:]    # 2-ая СС
print(b_num)

o_num = oct(num)[2:]    # 8-ая СС
print(o_num)

h_num = hex(num)[2:]    # 16-ая СС
print(h_num)