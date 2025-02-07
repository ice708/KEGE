from turtle import *

# pd() или pendown() - опустить хвост (перо)
# pu() или penup() - поднять хвост (перо)
# 
# Повороты
# left( градусы )
# right( градусы )
#
# Движение
# forward( величина )
# backward( величина )
# 
# goto(x, y) - переместить в координаты

speed(0) # максимальная скорость рисования
tracer(0) # отключить анимацию рисования
left(90) # задать начальное направление (в примере, вдоль оси Y)
# по умолчанию черепаха смотрит вдоль оси X
k = 20 # коэффициент для масштаба 1:1 для системы координат и отрисованной фигуры
screensize(1000, 1000) # размер окна с отрисованной графикой (для возможности скроллинга)

for i in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)
pu()
forward(1 * k)
right(90)
forward(5 * k)
left(90)
pd()
for i in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)
pu()

# отрисовка координатной сетки
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5)  # нарисовать точку размером 5

done() # ждать. не закрывать окно