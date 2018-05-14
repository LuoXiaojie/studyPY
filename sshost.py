#coding=utf-8
__metaclass__ = type
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
import socket

class Server(ThreadingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'got the connect from {0}'.format(addr)
        self.wfile.write('Thank you for connecting')

if __name__ == '__main__':
    host = socket.gethostname()
    port = 1238
    print 'get the host: {0} and the prot: {1}'.format(host, port)
    s = Server((host, port), Handler) #每当服务器接收一个客户机时都会将该客户机的处理交给类Handler处理.
    s.serve_forever()
       
