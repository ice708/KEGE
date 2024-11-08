for A in range(1,1000):
    A_is_ok = True
    for x in range(1000):
        for y in range(1000):
            if ((2 * x + y != 70) or (x < y) or (A < x)) == False:
                A_is_ok = False
                break
        if A_is_ok == False:
            break
    if A_is_ok == True:
        print(A)
        