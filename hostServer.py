#coding=utf-8
__metaclass__ = type
import socket

if __name__ == '__main__':

    s = socket.socket()

    host = socket.gethostname()
    port = 1235
    print 'get the host: {0} and the prot: {1}'.format(host, port)
    s.bind((host, port))
    s.listen(5)

    maxtime = 3
    cur = 0
    while True:
        if cur > maxtime:
            break
        cur += 1
        try:
            #返回客户端的套接字和客户端地址
            client, addr = s.accept()
            print addr
            client.send('Thanks for connecting')
        finally:
            client.close()
    s.close()
       
