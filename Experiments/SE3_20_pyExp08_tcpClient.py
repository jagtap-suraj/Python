# SE-3, 20, Suraj Jagtap

#Python Experiment No. 8

"""Write a python program to create sockets for information exchange between the client and server."""

#TCP/IP Client that recieves messages from server

import socket

def tcpClient():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'          
    port = 12355

    s.connect((host, port))
    msg=s.recv(1024)

    while msg:
        print('Recieved: '+msg.decode())
        msg=s.recv(1024)
    s.close()

if __name__ == '__main__':
    tcpClient()

