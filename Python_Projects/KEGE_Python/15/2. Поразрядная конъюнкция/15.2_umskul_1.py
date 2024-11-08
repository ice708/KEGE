for A in range(1000):
    A_is_True = True
    for x in range(1000):
        if ((x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))) == False:
            A_is_True = False
            break
    if A_is_True == True:
        print(A)
        break