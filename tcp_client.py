# tcp_client.py

from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#发起连接
server_addr = ('127.0.0.1',8888)
# server_addr = ('176.209.105.53',9999)
sockfd.connect(server_addr)


while True:
    data = input("发送>>")
    sockfd.send(data.encode())
    if not data:
        break
    data = sockfd.recv(1024)
    print("接收到：",data.decode())

#关闭套接字
sockfd.close()