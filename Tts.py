import pyttsx3
from gtts import gTTS
from playsound import playsound
from loquendo import LoquendoBot
import random
# import time
import os


class tts:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.loq = LoquendoBot()
        self.usuarios = {}
        file = open("users.txt", "r")
        str_usuarios = file.read()
        list_usuarios = str.split(str_usuarios, '\n')
        for line in list_usuarios:
            if line is not "":
                sep = line.index(' ')
                self.usuarios.update({line[0:sep] : line[sep+1:]})
        file.close()
        self.voices = ['HELENA', 'ZIRA', 'GOOGLE', 'LOQUENDO']

    def decir(self, user, msg):
        voice = None
        if user not in self.usuarios:
            voice = random.choice(['HELENA', 'GOOGLE', 'LOQUENDO'])
            self.usuarios[user] = voice
            file = open("users.txt", 'a')
            file.write(user + " " + voice)
            file.close()
        else:
            voice = self.usuarios[user]
        # voice = 'LOQUENDO'  # test
        # voice = 'GOOGLE'  # test
        # voice = 'ZIRA'  # test
        # voice = 'HELENA'  # test

        if(voice == 'GOOGLE'):
            sp = gTTS(user + " dice :" + msg, lang='es')
            file = 'C:/Temp/temp.mp3'
            sp.save(file)
            playsound(file)
            os.remove(file)
        elif(voice == 'HELENA'):
            self.engine.setProperty(
                'voice', self.engine.getProperty('voices')[0].id)
            self.engine.say(user + " dice :" + msg)
            self.engine.runAndWait()
        elif(voice == 'ZIRA'):
            self.engine.setProperty(
                'voice', self.engine.getProperty('voices')[1].id)
            self.engine.say(user + " says, " + msg)
            self.engine.runAndWait()
        elif(voice == 'LOQUENDO'):
            self.loq.decirT(user + " dice :" + msg)
        print(user + " -> " + voice)

    def updateFile(self):
        file = open('users.txt', 'w')
        str_users = ""
        
        for user in self.usuarios:
            str_users += user + ' ' + self.usuarios[user] + "\n"
        
        file.write(str_users)
        file.close()
            
