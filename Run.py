from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
import time
from Tts import tts
import re

s = openSocket()
joinRoom(s)

readbuffer = ""
speech = tts()

while True:

    time.sleep(.5)
    readbuffer = readbuffer + s.recv(1024).decode('utf-8')
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()

    print(time.time(), end=' ')

    for line in temp:
        print(line)
        
        # Necesario devolver un PONG cuando recibimos PING para mantener la conexión
        if line[0:4] == "PING":
            s.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))
            print("PONG")
        else:
            user = getUser(line)
            message = getMessage(line)

            if "!" == message[0]:
                if "testbot" in message[1:8]:
                    sendMessage(s, "Aqui estoy, loco")
                elif "voz" in message[1:4]:
                    if user not in speech.usuarios:
                        sendMessage(s, "@" + user + " Aún no tienes voz asignada, \
                                escribe un mensaje normal para que se te asigne una voz. \
                                Tambien puedes usar !cambiarvoz para elegir tu voz preferida")
                    else:
                        sendMessage(s, "@"+user+" Tu voz actual es " +
                                    speech.usuarios[user])
                elif "cambiarvoz" in message[1:11]:
                    voz = None
                    for v in speech.voices:
                        if v in message.upper():
                            voz = v
                            break
                    if voz is None:
                        print("voz none")
                        sendMessage(s, "Usa !cambiarvoz [VOZ] para cambiar tu voz del TTS. "
                                    + "Voces: LOQUENDO, HELENA, ZIRA(Inglés) y GOOGLE")
                    else:
                        speech.usuarios[user] = voz
                        sendMessage(s, "@" + user +
                                    " Tu voz se ha cambiado a " + voz)
                        speech.updateFile()
                
                elif "tts" in message[1:4]:
                    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
                    pattern = re.compile(regex)
                    if pattern.search(message) is None:
                        speech.decir(user, message[5:])
                    else:
                        sendMessage(s, "@" + user + " No puedes usar links en tts.")