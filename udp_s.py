import socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind(('127.0.0.1',8000))
print('UDP编程')
print('等待节点连接......')
while 1:
    data,address=serversocket.recvfrom(256)
    if not data :break
    print('接收自: ',address)
    print('接收的数据为：',repr(data))
    print('回复节点：: ',repr(data))
    serversocket.sendto(data, address)
serversocket.close()
