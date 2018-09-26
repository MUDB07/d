# tcp_client.py

from socket import *


sockfd = socket(AF_INET,SOCK_STREAM)


server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)


while True:
    print("1.查看所有文件")
    data = input("发送>>")
    sockfd.send(data.encode())
    if not data:
        break
    data = sockfd.recv(1024)
    print("接收到：",data.decode())


sockfd.close()