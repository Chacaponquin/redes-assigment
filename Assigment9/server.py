from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverSocket.bind(('', 8080))
serverSocket.listen(5) 

while True:
   print('Ready to serve...')
   connectionSocket, addr = serverSocket.accept()

   try:
       message = connectionSocket.recv(1024).decode()

       if len(message.split()):
           filename = message.split()[1]
           print('File: ' + filename)

           f = open(filename[1:])
           outputdata = f.read()

           connectionSocket.send('HTTP/1.1 200 OK\n\n'.encode())

           connectionSocket.send(outputdata.encode())
           connectionSocket.send("\r\n".encode())

           print()

       connectionSocket.close()
   except IOError:
       connectionSocket.send('HTTP/1.1 404 NOT FOUND\n\n'.encode())
       connectionSocket.close()


serverSocket.close()
sys.exit()