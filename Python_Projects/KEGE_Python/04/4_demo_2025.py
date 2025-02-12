def fano(a, b): # проверка условия Фано
    l = min(len(a), len(b)) # сколько знаков проверяем
    return a[:l] != b[:l] # сравнение срезов двух кодов


codes = ['1001','11']

for i in range(1,4+1): # длина генерируемого двоичного кода
    for x in range(2**i):
        pfx = bin(x)[2:].zfill(i) # генерация всех двоичных кодов разной длины (дерево)
        if all(fano(pfx,c) for c in codes): # проверка условия Фано со значениями списка "codes"
            print(pfx)