from chatterbot  import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition as sr

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
engine = pyttsx3.init()
r = sr.Recognizer()
# for files in os.listdir('/Users/gaurang/Python_Practice/Corpuses/chatterbot-corpus/chatterbot_corpus/data/english/'):
#     data = open('/Users/gaurang/Python_Practice/Corpuses/chatterbot-corpus/chatterbot_corpus/data/english/' + files,'r').readlines()
#     bot.train(data)
initial_text = 'Hi this is Alexa!, Please give me a command'
engine.say(initial_text)
engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print("Speak Anything.")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
            if text != 'bye':
                print(text)
                reply = bot.get_response(text)
                print('Chatbot : {}'.format(reply))
                # engine.say(reply)
                # engine.runAndWait()
            else:
                break
        except:
            print("sorry could not here you.")


