def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024).decode('utf-8')
        temp = str.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    print("Successfully joined chat")


def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
