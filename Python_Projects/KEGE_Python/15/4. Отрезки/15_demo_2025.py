P = list(range(15, 41)) # отрезок P = [15;40]
Q = list(range(21, 64)) # отрезок Q = [21;63]
A = [] # если МИН(А), то А пустой

for x in range(1, 100):
    if ((x in P) <= (((x in Q) and not (x in A)) <= (not (x in P)))) == False:
        A.append(x)

print('A = ', A)    # отрезок А с его точками
print('Длина А: ', A[-1] - A[0]) # длина отрезка А, ЕСЛИ крайние точки включены в отрезки P и Q
print('Длина А: ', max(A) - min(A))

# ! если крайние точки отрезка А НЕ попадают в отрезки P и Q, 
# ! то взять ближайшие значения для крайних точек отрезка А.

# Умскул. Разбор типов задач №15
# https://www.youtube.com/live/tHNEptDgud4?si=hDEmuATKNyhR8dFG