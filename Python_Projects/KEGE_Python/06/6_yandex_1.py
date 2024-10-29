# №1
# Какая цифра получится?
# Направо 30, Вперед 45, Налево 120, Вперед 25
# Ответ: 7

# Решение:
# from turtle import *
# right(30)
# forward(45)
# left(120)
# forward(25)
# done()

# ---------------------

# https://education.yandex.ru/ege/task/a10ac35a-d156-4410-b805-f4891aab9345

from turtle import *
tracer(0)
k = 20
screensize(10000,10000)
left(90)
for i in range(2):
    forward(7*k)
    right(90)
    forward(14*k)
    right(90)
pu()
backward(5*k)
left(90)
forward(3*k)
right(90)
pd()
for i in range(4):
    forward(8*k)
    right(90)
pu()
forward(10*k)
pd()
for i in range(4):
    forward(10*k)
    right(90)
pu()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3)

done()
