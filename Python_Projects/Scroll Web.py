import keyboard
import time
import threading

# Флаг для управления циклом
running = False

def press_page_down():
    global running
    while running:
        keyboard.press_and_release('pagedown')  # Нажимаем клавишу Page Down
        time.sleep(3)  # Ждем 3 секунды

def toggle():
    global running
    running = not running  # Переключаем состояние
    if running:
        print("Запуск нажатий Page Down...")
        threading.Thread(target=press_page_down).start()  # Запускаем поток
    else:
        print("Остановка нажатий Page Down...")

# Назначаем обработчик нажатия пробела
keyboard.add_hotkey('space', toggle)

print("Нажмите пробел для запуска/остановки программы.")
keyboard.wait('esc')  # Программа будет работать, пока не будет нажата клавиша 'esc'
 