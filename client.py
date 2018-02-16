import socket
from struct import *

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
sock.send(bytes('hello world!', encoding='utf-8'))

data = sock.recv(1024)
sock.close()

print(data)