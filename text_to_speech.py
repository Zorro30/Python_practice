# from gtts import gTTS
# # also do, brew install mpg321
# import os



# language = 'en'

# obj = gTTS(text = 'my_text', lang = language, slow = False)

# obj.save("welcome.mp3")

# os.system("mpg321 welcome.mp3")
# # os.system('rm -rf welcome1.mp3')

import pyttsx3
engine = pyttsx3.init()
my_text = 'Hello I am a Patbot. Please give me some command.'
engine.say(my_text)

engine.runAndWait()