import wikipedia

# Установка языка на русский
wikipedia.set_lang("ru")

# Запрос от пользователя
input_query = input("Введите запрос: ")

try:
    # Получение аннотации статьи
    summary = wikipedia.summary(input_query)
    print(summary)
except wikipedia.exceptions.DisambiguationError as e:
    print(f"Неоднозначный запрос: {e.options}")
except wikipedia.exceptions.PageError:
    print("Статья не найдена.")