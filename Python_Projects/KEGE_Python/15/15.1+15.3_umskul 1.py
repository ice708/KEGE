def DEL(n, m):
    return n % m == 0

for A in range(1, 1000):
    for x in range(1, 1000):
        if ((DEL(x, 2) <= (not DEL(x, 3))) or (x + A >= 100)) == False:
            break
    else:
        print(A)
        break