import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL


def openSocket():

    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(("PASS " + PASS + "\r\n").encode('utf-8'))
    s.send(("NICK " + IDENT + "\r\n").encode('utf-8'))
    s.send(("JOIN #" + CHANNEL + "\r\n").encode('utf-8'))
    return s


def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode('utf-8'))
    print("Sent: " + messageTemp)
