import turtle

# Функция для проверки, находится ли точка внутри многоугольника
def is_point_in_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

# Инициализация черепахи
turtle.speed(0)  # Установить максимальную скорость
turtle.penup()
turtle.goto(-3, -4)  # Начальная позиция
turtle.setheading(90)  # Направление вверх
turtle.pendown()

# Поворот направо на 30 градусов
turtle.right(30)

# Список для хранения координат вершин многоугольника
polygon = []

# Повторяем 10 раз
for _ in range(10):
    # Движение вперед на 14
    turtle.forward(14)
    # Сохраняем текущую позицию
    polygon.append(turtle.position())
    # Поворот направо на 120 градусов
    turtle.right(120)

# Закрываем контур
polygon.append(polygon[0])  # Добавляем первую точку в конец для замыкания

# Подсчет целочисленных точек с отрицательными координатами внутри многоугольника
count = 0
for x in range(-3, 1):  # x от -3 до 0 (включительно)
    for y in range(-4, 1):  # y от -4 до 0 (включительно)
        if is_point_in_polygon(x, y, polygon):
            count += 1

# Вывод результата
print("Количество целочисленных точек с отрицательными координатами внутри контура:", count)

# Завершение работы turtle
turtle.done()
print(count)