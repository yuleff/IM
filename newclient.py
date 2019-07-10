
import socket

import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("127.0.0.1",8888))

true=True

def rec(s):

    global true

    while true:

        t=s.recv(1024).decode("utf8")  #客户端也同理

        if t == "exit":

            true=False

        print(t)

trd=threading.Thread(target=rec,args=(s,))

trd.start()

while true:

    t=input()

    s.send(t.encode('utf8'))

    if t == "exit":

        true=False

s.close()
