def DEL(n, m):
    return n % m == 0

# for A in range(1000, 0, -1):
#     A_is_ok = True
#     for x in range(1000, 0, -1):
#         if ((not DEL(x, A)) <= (DEL(x, 6) <= (not (DEL(x, 9))))) == False:
#             A_is_ok = False
#             break
#     if A_is_ok == True:
#         print(A)
#         break


for A in range(1000, 0, -1):
    for x in range(1000, 0, -1):
        if ((not DEL(x, A)) <= (DEL(x, 6) <= (not (DEL(x, 9))))) == False:
            break
    else:
        print(A)
        break