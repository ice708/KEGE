# № 18169
# https://kompege.ru/task

# Значение арифметического выражения 3**2000+3**10−х, 
# где х – натуральное число, записали в троичной системе счисления. 
# Определите наименьшее значение x, 
# при котором троичная запись значения данного выражения содержит 2000 цифр «2».

# Ответ: 59050
# Время выполнения программы: 164.63382110000384 секунд

import time
start_time = time.perf_counter()

for x in range(100000):
    num = 3 ** 2000 + 3 ** 10 - x
    count = 0
    while num > 0:
        if num % 3 == 2:
            count += 1
        num //= 3
    if count == 2000:
        print(x)
        break

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд")