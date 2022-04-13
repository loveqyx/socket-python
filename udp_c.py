import socket
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('连接成功！')
while 1:
    data=input('请输入:')
    clientsocket.sendto(data.encode(),('127.0.0.1',8000))
    if not data:break
    newdata=clientsocket.recvfrom(256)
    print('接收自Server: ',repr(newdata))
clientsocket.close()
