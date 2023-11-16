import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)

for i in range(1, 11):
   message = f"{i},{time.time()}"

   HOST_IP = "10.0.0.1"
   LOCALHOST_IP = "127.0.0.1"
   client_socket.sendto(message.encode(), (HOST_IP, 12000))

   try:
       data, addr = client_socket.recvfrom(1024)
       print(i)
       print(f"Response from server: {data.decode()}")
       
       sequence_number, send_time = data.decode().split(',')
       rtt = time.time() - float(send_time)
       print(f"Round trip time: {rtt} seconds\n")
   except socket.timeout:
       print(i)
       print("Request timed out\n")