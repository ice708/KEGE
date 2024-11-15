file = open("C:/KEGE/demo_2025_17.txt")     #открываем файл

num_in_file = []    # создаем пустой список для чисел из файла

# добавляем числа из файла в список
for x in file:
    num_in_file.append(int(x))

min_num = min(num_in_file) # находим минимальное число из последовательности чисел из файла
num_list = []   # создаем пустой список для сумм подходящих пар чисел

# добавляем в список суммы чисел, которые подходят по условию
for i in range(len(num_in_file)-1):
    if num_in_file[i] % 16 == min_num or num_in_file[i + 1] % 16 == min_num:
        num_list.append(num_in_file[i] + num_in_file[i + 1])

print(len(num_list))    # количество пар чисел, подходящих по условию
print(max(num_list))    # максимальное значение суммы чисел 