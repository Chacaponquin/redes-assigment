import http.client
import sys

def client(server, port, path):
   connection = http.client.HTTPConnection(server, port)
   connection.request("GET", path)
   response = connection.getresponse()
   print("Status: {} and reason: {}".format(response.status, response.reason))
   data = response.read()

   print(data.decode())

   connection.close()


if __name__ == "__main__":
   server = sys.argv[1]
   port = int(sys.argv[2])
   path = sys.argv[3]

   client(server, port, path)