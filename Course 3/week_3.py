import socket
import urllib.request,urllib.error,urllib.parse

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()   #to convert Unicode to UTF 8
mySocket.send(cmd)

while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break

    print(data.decode())

mySocket.close()

fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

for line in fhand:
    print(line.decode().strip())