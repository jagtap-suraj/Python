# SE-3, 20, Suraj Jagtap

#Python Experiment No. 8

"""Write a python program to create sockets for information exchange between the client and server."""

# TCP/IP server that sends messages to client

import socket

def tcpServer():
    s = socket.socket()
    host = 'localhost'          
    port = 12355
    s.bind((host, port))

    s.listen(5)

    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(b'Hello client, How are you')
    msg='Bye!'
    c.send(msg.encode())

    c.close()

if __name__ == '__main__':
    tcpServer()

