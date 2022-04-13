import socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 1234))
serversocket.listen(1)
clientsocket, clientaddress=serversocket.accept()
print('这是TCP的service')
print('IP地址及端口号: ', clientaddress)
while 1:
    data = clientsocket.recv(256)
    print('从连接接收到: ', repr(data))
    clientsocket.send(data)
clientsocket.close()
serversocket.close()

