# №2 ФИПИ Демо 2024
from itertools import *

print('x y z w')

for i in product('01', repeat=4):
    if (((int(i[3]) <= int(i[1])) <= int(i[0])) or not int(i[2])) == 0:
        print(*i)