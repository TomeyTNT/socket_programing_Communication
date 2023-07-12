from socket import *
serverName ="localhost"
serverPort = 5000
clientSocket = socket (AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input filename:')
clientSocket.sendall(sentence.encode("utf-8"))
modifiedSentence = b""
while True:
    data = clientSocket.recv(1024)
    if not data:
        break
    modifiedSentence += data

f = open("MyReverseFile.txt", "w")

modifiedSentences = modifiedSentence.decode("utf-8").split("\n")
for sentence in modifiedSentences:
    if sentence != "file not found":
        s = sentence.split()[::-1]
        l = []
        for i in s:

            l.append(i)

        f.writelines(" ".join(l))
        f.writelines("\n")
    else:
        print('From Server:', sentence)

clientSocket.close()
