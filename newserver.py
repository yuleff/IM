
import socket

import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("127.0.0.1",8888))

s.listen(2)

sock,addr=s.accept()

true=True

def rec(sock):

    global true

    while true:

        t=sock.recv(1024).decode('utf8')  #函数的核心语句就一条接收方法

        if t == "exit":

            true=False

        print(t)

trd=threading.Thread(target=rec,args=(sock,))

trd.start()

while true:

    t=input()

    sock.send(t.encode('utf8'))

    if t == "exit":

        true=False

s.close()
