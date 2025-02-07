def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []
    except ValueError:
        print(f"В файле {filename} содержатся не только числа.")
        return []

# Пример использования
filename = 'C:\Users\Kirill\Documents\GitHub_repo\KEGE\Python_Projects\input.txt'
numbers = read_numbers_from_file(filename)
print(numbers)