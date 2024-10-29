import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Инициализация синтезатора речи
engine = pyttsx3.init()

# Установка языка Википедии на русский
wikipedia.set_lang("ru")

# Получение доступных голосов
voices = engine.getProperty('voices')

# Выбор голоса (например, 0 - первый голос, 1 - второй голос и т.д.)
# Вы можете прослушать доступные голоса и выбрать нужный
engine.setProperty('voice', voices[0].id)  # Замените 0 на 1 или другой индекс для смены голоса
voices = engine.getProperty('voices')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='ru-RU')
            print(f"Вы сказали: {command}")
            return command
        except sr.UnknownValueError:
            print("Не удалось распознать речь.")
            return ""
        except sr.RequestError:
            print("Ошибка сервиса распознавания.")
            return ""

def respond_to_command(command):
    command = command.lower()
    
    if "привет" in command:
        speak("Привет! Как я могу помочь?")
    
    elif "время" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"Сейчас {current_time}")
    
    elif "информация" in command:
            speak("О чем вы хотите узнать?")
            topic = listen()
            try:
                summary = wikipedia.summary(topic, sentences=1)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Существует несколько значений. Пожалуйста, уточните.")
            except wikipedia.exceptions.PageError:
                speak("Извините, я не смог найти информацию.")
            except Exception as e:
                speak("Произошла ошибка при поиске информации.")
    
    elif "пока" in command:
        speak("До свидания!")
        return False
    
    return True

def main():
    speak("Здравствуйте! Я ваш голосовой помощник.")
    running = True
    while running:
        command = listen()
        running = respond_to_command(command)

if __name__ == "__main__":
    main()
