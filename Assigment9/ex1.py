import threading

from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', 8080))
serverSocket.listen(5)


def handle_client(connectionSocket):
   try:
       message = connectionSocket.recv(1024).decode()

       if len(message.split()):
           filename = message.split()[1]
           f = open(filename[1:])
           print('File: ' + filename)

           output = f.read()

           connectionSocket.send('HTTP/1.1 200 OK\n\n'.encode())

           connectionSocket.send(output.encode())
           connectionSocket.send("\r\n".encode())

           print()
   except IOError:
       connectionSocket.send('HTTP/1.1 404 NOT FOUND\n\n'.encode())
   finally:
       connectionSocket.close()

while True:
   print('Ready to serve...')
   connectionSocket, addr = serverSocket.accept()
   client_thread = threading.Thread(target=handle_client, args=[connectionSocket])
   client_thread.start()

   
serverSocket.close()
sys.exit()
