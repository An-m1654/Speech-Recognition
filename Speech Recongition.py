import speech_recognition as sr
import webbrowser as web

speech = sr.Recognizer()
while True:
    print("Python is listening...")
    input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    print(f'You just said {input}.')
    if input == "stop listening":
        print('Goodbye!')
        break
    elif "search" in input:
        input = input.replace("search ", "")
        web.get('C:/Users/holun_000/AppData/Local/Programs/Opera GX/launcher.exe %s').open(f"https://www.google.com/search?q={input}")
    elif "website" in input:
        input = input.replace("website ", "")
        web.get('C:/Users/holun_000/AppData/Local/Programs/Opera GX/launcher.exe %s').open(input)
