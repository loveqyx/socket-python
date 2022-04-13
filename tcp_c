import socket
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1',1234))
print('连接成功！')
while 1:
    data=input('请输入:')
    clientsocket.send(data.encode())
    if not data:break
    newdata=clientsocket.recv(256)
    print('来自Server的回复:',repr(newdata))
clientsocket.close()

