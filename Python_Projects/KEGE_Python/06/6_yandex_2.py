# https://education.yandex.ru/ege/task/ccdad552-1139-46d1-8746-ae5e5e513a3c

from turtle import *
tracer(0)
k = 20
screensize(5000,5000)

left(90)
# Повтори 2 [Вперёд 8 Направо 90 Вперёд 16 Направо 90]
for i in range(2):
    forward(8 * k)
    right(90)
    forward(16 * k)
    right(90)
# Повтори 4 [Вперёд 8 Направо 120]
for i in range(4):
    forward(8 * k)
    right(120)
pu()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(5)
done()
