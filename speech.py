import speech_recognition as sr
import webbrowser

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Speak Anything.")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            if text == 'bye':
                break
            print("You said: {}".format(text))
        except:
            print("sorry could not here you.")
        
just checking for future purpose
if text == "Gaurang":
    webbrowser.open('http://www.google.com')