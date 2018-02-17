#https://www.youtube.com/watch?v=wV2WavaPNrU&feature=youtu.be&list=PLrCZzMib1e9pg7ZLIOhmGSlmkMf8yEOLZ&t=2651
import socket
import os
import sys

server_socket = socket.socket()
server_socket.bind(('', 9090))
server_socket.listen(10)

# while True:
#     client_socket, remote_address = server_socket.accept()
#     child_pid = os.fork()
#     if child_pid == 0:
#         request_data = client_socket.recv(1024)
#         #if not request_data or request_data == "close":
#         #    break
#         client_socket.send(request_data)
#         client_socket.close()
#         sys.exit()
#     else:
#         client_socket.close()
# server_socket.close()

for i in range(4):
    child_pid = os.fork()
    if child_pid == 0:
        try:
            while True:
                client_socket, remote_address = server_socket.accept()
                request_data = client_socket.recv(1024)
                client_socket.send(request_data)
                client_socket.close()
        except KeyboardInterrupt:
            sys.exit()

try:
    os.waitpid(-1, 0)
except KeyboardInterrupt:#
    sys.exit()
