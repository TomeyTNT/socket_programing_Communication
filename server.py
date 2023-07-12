from socket import *

serverPort = 5000
serverSocket = socket (AF_INET,SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)
print ('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode("utf-8")

    try:
        with open(sentence) as f:
            lines = f.readlines()
            yrs_string = '' # create a variable yrs_string to hold the digits of years
            for line in lines: # create a loop that adds each line of digits to yrs_string
                yrs_string = line.rstrip() #.rstrip() removes the newline character from each line
                connectionSocket.sendall(yrs_string.encode("utf-8") + b"\n")


    except FileNotFoundError:
        connectionSocket.sendall("file not found".encode("utf-8"))
   


    connectionSocket.close()
