#!/usr/bin/python 

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Enter The ip Address: ")
port = int(input("Enter The Port Number: "))

def portscanner(port):
    if sock.connect_ex((host,port)):
        print('Port ',port,' is closed')

    else:
        print('Port ',port,' is open!')

portscanner(port)