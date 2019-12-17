# lesson https://www.py4e.com/html3/12-network
# video: https://www.coursera.org/learn/python-network-data/lecture/E4vSF/worked-example-sockets-chapter-12
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

# Code: http://www.py4e.com/code3/socket1.py