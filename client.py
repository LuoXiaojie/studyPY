#coding=utf-8
__metaclass__ = type
import socket

if __name__ == '__main__':

    try:
        s = socket.socket()

        host = socket.gethostname()
        port = 1238
        print 'get the host: {0} and the prot: {1}'.format(host, port)
        #连接客户端。
        s.connect((host, port))
        print s.recv(1024)
    except:
        print 'connect meet a except'
    finally:
        s.close()

        