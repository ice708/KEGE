# очень внимательно с крайними точками искомого отрезка

f_usl = 1
A = 0
otrezok = [] # необязательная переменная. искомый отрезок

for x in [k * 0.25 for k in range(-10000, 10000)]:
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    f = P <= ((Q and (not A)) <= (not P))
    if f != f_usl:
        print(x)
        otrezok.append(x) # все точки в искомом отрезке

print(abs(otrezok[0] - otrezok[-1])) # длина отрезка.