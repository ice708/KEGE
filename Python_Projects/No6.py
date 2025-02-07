def generate_combinations(arr):
    n = len(arr)
    result = []

    def backtrack(start, current_combination):
        if start == n:
            if current_combination and current_combination != [arr]:  # Проверка на полную комбинацию
                result.append(current_combination)
            return
        
        for end in range(start + 1, n + 1):
            # Формируем комбинацию из соседних чисел
            new_combination = arr[start:end]
            backtrack(end, current_combination + [new_combination])

    backtrack(0, [])
    return result

# Ввод данных
n = int(input("Введите длину списка (n): "))
k = int(input("Введите количество элементов списка (k): "))
numbers = list(map(int, input(f"Введите {n} чисел через пробел: ").split()))

combinations = generate_combinations(numbers)

max_sum_combo = None
min_sum_combo = None
max_sum = float('-inf')
min_sum = float('inf')

# Выводим все комбинации и находим максимальную и минимальную суммы вложенных списков
for combo in combinations:
    if len(combo) == k:
        print(combo)
        
        # Находим максимальную и минимальную сумму среди вложенных списков
        current_sums = [sum(sublist) for sublist in combo]
        current_max_sum = max(current_sums)
        current_min_sum = min(current_sums)
        
        # Проверяем на максимальную и минимальную сумму
        if current_max_sum > max_sum:
            max_sum = current_max_sum
            max_sum_combo = combo
        if current_min_sum < min_sum:
            min_sum = current_min_sum
            min_sum_combo = combo

# Выводим список с максимальной и минимальной суммой
if max_sum_combo is not None:
    print(f"Список с максимальной суммой: {max_sum_combo}, Сумма: {max_sum}")
if min_sum_combo is not None:
    print(f"Список с минимальной суммой: {min_sum_combo}, Сумма: {min_sum}")

# Находим комбинацию с наибольшей разностью между максимальной и минимальной суммой
max_difference = float('-inf')
result_combo = None

for combo in combinations:
    if len(combo) == k:
        current_sums = [sum(sublist) for sublist in combo]
        current_max_sum = max(current_sums)
        current_min_sum = min(current_sums)
        difference = current_max_sum - current_min_sum
        if difference > max_difference:
            max_difference = difference
            result_combo = combo

# Отображаем результат
print("Результат:")
if result_combo is not None:
    print(result_combo)