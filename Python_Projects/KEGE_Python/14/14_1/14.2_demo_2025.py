alphabet = '0123456789ABCDEFGHI'

for x in alphabet:
    f = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if f % 18 == 0:
        print(f // 18)