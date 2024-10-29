# Движок цепляет голоса из настроек TTS в Windows, так что дополнительные голоса нужно устанавливать:
# https://support.microsoft.com/en-us/topic/download-languages-and-voices-for-immersive-reader-read-mode-and-read-aloud-4c83a8d8-7486-42f7-8e46-2b0fdf753130

import pyttsx3

# Инициализация синтезатора речи
engine = pyttsx3.init()

# Получение доступных голосов
voices = engine.getProperty('voices')

# Прослушивание каждого доступного голоса
for index, voice in enumerate(voices):
    engine.setProperty('voice', voice.id)
    engine.say(f"Это голос номер {index}.")
    engine.runAndWait()

# Завершение работы синтезатора
engine.stop()

# engine.runAndWait()
