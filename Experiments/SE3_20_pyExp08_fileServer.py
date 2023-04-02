# SE-3, 20, Suraj Jagtap

#Python Experiment No. 8

"""Write a python program to create sockets for information exchange between the client and server."""

# File server that sends file contents to client

import socket

def fileServer():
    host = 'localhost'
    port = 6767
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    fname = c.recv(1024)
    fname = str(fname.decode())
    try:
        f = open(fname, 'rb')
        content = f.read()
        c.send(content)
        f.close()
    except FileNotFoundError:
        c.send(b'File does not exist')
    c.close()

if __name__ == '__main__':
    fileServer()
