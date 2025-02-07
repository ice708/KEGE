def generate_combinations(arr):
    n = len(arr)  # Получаем длину входного массива
    result = []  # Список для хранения всех комбинаций

    def backtrack(start, current_combination):
        # Функция для генерации комбинаций с использованием метода обратного отслеживания
        if start == n:  # Если достигли конца массива
            # Проверка на непустую комбинацию и чтобы не добавлять полный массив
            if current_combination and current_combination != [arr]:
                result.append(current_combination)  # Добавляем комбинацию в результат
            return
        
        # Генерируем комбинации, перебирая возможные конечные индексы
        for end in range(start + 1, n + 1):
            # Формируем новую комбинацию из соседних чисел
            new_combination = arr[start:end]
            # Рекурсивно вызываем backtrack для следующего индекса
            backtrack(end, current_combination + [new_combination])

    backtrack(0, [])  # Запускаем backtrack с начальным индексом 0 и пустой комбинацией
    return result  # Возвращаем все найденные комбинации

# Ввод данных от пользователя
n, k = map(int, input("Введите длину списка (n) и количество элементов списка (k): ").split())
# n = int(input("Введите длину списка (n): "))  # Длина списка
# k = int(input("Введите количество элементов списка (k): "))  # Количество элементов в комбинации
numbers = list(map(int, input(f"Введите {n} чисел через пробел: ").split()))  # Ввод чисел

# Генерируем все комбинации
combinations = generate_combinations(numbers)

max_sum_combo = None  # Переменная для хранения комбинации с максимальной суммой
min_sum_combo = None  # Переменная для хранения комбинации с минимальной суммой
max_sum = float('-inf')  # Инициализируем максимальную сумму как отрицательную бесконечность
min_sum = float('inf')  # Инициализируем минимальную сумму как положительную бесконечность

# Выводим все комбинации и находим максимальную и минимальную суммы вложенных списков
for combo in combinations:
    if len(combo) == k:  # Проверяем, соответствует ли длина комбинации k
        print(combo)  # Выводим текущую комбинацию
        
        # Находим суммы вложенных списков
        current_sums = [sum(sublist) for sublist in combo]
        current_max_sum = max(current_sums)  # Максимальная сумма среди вложенных списков
        current_min_sum = min(current_sums)  # Минимальная сумма среди вложенных списков
        
        # Проверяем на максимальную и минимальную сумму
        if current_max_sum > max_sum:
            max_sum = current_max_sum  # Обновляем максимальную сумму
            max_sum_combo = combo  # Обновляем комбинацию с максимальной суммой
        if current_min_sum < min_sum:
            min_sum = current_min_sum  # Обновляем минимальную сумму
            min_sum_combo = combo  # Обновляем комбинацию с минимальной суммой

# Выводим список с максимальной и минимальной суммой
if max_sum_combo is not None:
    print(f"Список с максимальной суммой: {max_sum_combo}, Сумма: {max_sum}")
if min_sum_combo is not None:
    print(f"Список с минимальной суммой: {min_sum_combo}, Сумма: {min_sum}")

# Находим комбинацию с наибольшей разностью между максимальной и минимальной суммой
max_difference = float('-inf')  # Инициализируем максимальную разность как отрицательную бесконечность
result_combo = None  # Переменная для хранения комбинации с наибольшей разностью

for combo in combinations:
    if len(combo) == k:  # Проверяем, соответствует ли длина комбинации k
        current_sums = [sum(sublist) for sublist in combo]  # Суммы вложенных списков
        current_max_sum = max(current_sums)  # Максимальная сумма
        current_min_sum = min(current_sums)  # Минимальная сумма
        difference = current_max_sum - current_min_sum  # Вычисляем разность
        
        # Проверяем, является ли текущая разность максимальной
        if difference > max_difference:
            max_difference = difference  # Обновляем максимальную разность
            result_combo = combo  # Обновляем комбинацию с наибольшей разностью

# Результат
print("Результат:")
if result_combo is not None:
    print(result_combo)
    print("Оптимальное разбиение:", max_difference)