'''
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(end='\t')
for i in range(c, d + 1):
    print(i, end='\t')
print()
for i in range(a, b+1):
    print(i, end='\t')
    for j in range(c, d+1):
        print(i * j, end='\t')
    print()

n = int(input())
s = [i for i in range(n+1) for j in range(i)]
print(s)
for i in range(n):
    print(int(s[i]), end=' ')
    
x = []
n = int(input())
for i in range(n+1):
    x += (i*[i])
print(' '.join(map(str, x[:n])))
или print(*x[:n])

lst = [int(i) for i in input().split()]
pos = []
x = int(input())
if x in lst:
    n = 0
    while (x in lst[n:]) and (lst.index(x, n) != (len(lst) - lst[::-1].index(x))):
        poserver_socket.append(lst.index(x, n))
        n = pos[-1] + 1
    print(*pos)
else:
    print("Отсутствует")
    
      [int(input()) for i in range(int(input()))]
lst = [int(i) for i in input().split()]
pos = []
x = int(input())
if x in lst:
    for ind, val in enumerate(lst):
        if val == x:
            poserver_socket.append(ind)
    #print(*[i for i in range(len(lst)) if lst[i]==x])
else:
    print("Отсутствует")
    

def p(a, b, *args):
    print(a, ' = a')
    print(b, ' = b')
    print(type(args), args)
    for arg in args:
        print(arg, type(arg))
s = {'t': 3, 'f': 5, 'z': 6}
p(2,5, s)'''

import socket

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 2222))
server_socket.listen(10)

while True:
    client_socket, addr = server_socket.accept()
    while True:
        data = client_socket.recv(1024)
        if not data or data == "close":
            break
        client_socket.send(data)
    client_socket.close()


# 1) vim server_socket.py
# 2) вбиваем наш код
# 3) жмём esc (затем жмем кнопку close terminal)
# 4) вбиваем :save server_socket.py (затем жмем кнопку close terminal)
# 5) вбиваем :q  (затем жмем кнопку close terminal)
# 6# ) в консоль вводим python server_socket.py im
# client
# req  = "Hello tcp!"
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.connect(('127.0.0.1', 1941))
# server_socket.send(req.encode())
# rsp = server_socket.reqv(1024)
# server_socket.close()
