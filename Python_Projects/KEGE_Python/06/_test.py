# № 9829 Основная волна 27.06.23 (Уровень: Средний)
# Направо 90
# Повтори 3 [Направо 45 Вперёд 10 Направо 45]
# Направо 315 Вперёд 10
# Повтори 2 [Направо 90 Вперёд 10].
from turtle import *

speed(0) # максимальная скорость рисования
tracer(0) # отключить анимацию рисования
screensize(1000, 1000)
k = 5

left(90)

pd()
right(90)

for i in range(3):
    right(45)
    forward(10 * k)
    right(45)

right(350)
forward(10 * k)

for i in range(2):
    right(90)
    forward(10 * k)

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5)

done()