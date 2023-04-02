# SE-3, 20, Suraj Jagtap

#Python Experiment No. 8

"""Write a python program to create sockets for information exchange between the client and server."""

# A Client that sends and recieves data

import socket

def fileClient():
    host = 'localhost'
    port = 6767

    s = socket.socket()         
    s.connect((host, port))

    filename = input('Enter Filename: ')
    s.send(filename.encode())

    msg = s.recv(1024)

    while msg:
        print('Recieved: '+msg.decode())
        msg = s.recv(1024)

    s.close()

if __name__ == '__main__':
    fileClient()
