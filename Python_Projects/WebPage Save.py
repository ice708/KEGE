import webbrowser
import time
import pyautogui

# Генерация и открытие страниц
# num = [233, 234, 236, 237, 544]
for page in range(226, 385):
# for page in num:
    # Формирование ссылки
    url = f'https://www.litres.ru/pages/get_pdf_page/?file=94435940&page={page}&rt=w1900&ft=gif'
    
    # Открытие ссылки в браузере
    webbrowser.open(url)
    
    # Задержка для загрузки страницы
    time.sleep(5)  # Увеличьте время, если страница загружается медленно

    pyautogui.keyDown('ctrl')  # Удерживаем Ctrl
    pyautogui.press('s')        # Нажимаем W
    pyautogui.keyUp('ctrl')     # Отпускаем Ctrl
    # # Перемещение мыши к изображению (может потребоваться настроить координаты)
    # # Вам нужно будет вручную определить координаты изображения на экране
    # # Например, если изображение находится в центре экрана:
    # pyautogui.moveTo(960, 540)  # Замените на координаты изображения
    # time.sleep(1)

    # # Вызов контекстного меню
    # pyautogui.rightClick()
    # time.sleep(1)

    # # Выбор "Сохранить изображение как..." (может потребоваться настроить)
    # pyautogui.press('down')  # Нажмите 'down' для выбора пункта меню
    # pyautogui.press('down')  # Нажмите 'down' ещё раз
    # pyautogui.press('enter')  # Нажмите 'enter' для подтверждения

    # Задержка для открытия диалогового окна сохранения
    time.sleep(3)

    # Ввод имени файла (только номер страницы в трехзначном формате)
    filename = f'{page:03d}'  # Имя файла в трехзначном формате
    pyautogui.typewrite(filename)
    time.sleep(2)

    # Нажмите 'enter' для сохранения
    pyautogui.press('enter')

    # Задержка для завершения сохранения
    time.sleep(1)

    # Задержка перед закрытием вкладки
    time.sleep(1)  # Убедитесь, что фокус на браузере

    # Закрытие вкладки с удерживанием Ctrl
    pyautogui.keyDown('ctrl')  # Удерживаем Ctrl
    pyautogui.press('w')        # Нажимаем W
    pyautogui.keyUp('ctrl')     # Отпускаем Ctrl

    # Задержка перед открытием следующей страницы
    time.sleep(1)
