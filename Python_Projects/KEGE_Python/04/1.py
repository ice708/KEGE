# Открываем входной файл для чтения
with open('input.txt', 'r') as infile:
    # Читаем строку из файла и разбиваем её на части
    line = infile.readline()
    A, B = map(int, line.split())  # Преобразуем строки в целые числа

# Вычисляем сумму
result = A + B

# Открываем выходной файл для записи
with open('output.txt', 'w') as outfile:
    # Записываем результат в файл
    outfile.write(str(result))
