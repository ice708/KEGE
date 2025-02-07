for num in range(1700, 37000):
    for a in range(1,50):
        for b in range(1,50):
            for x in range(1,50):
                for y in range(1,50):
                    if (num == a ** 3 + b ** 3 == x ** 3 + y ** 3) and (a != b != x != y):
                        print (f"{num}={a}^3+{b}^3={x}^3+{y}^3")
                        break