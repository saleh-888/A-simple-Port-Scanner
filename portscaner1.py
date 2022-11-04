#!/usr/bin/python
import socket

def welcom():
    print('''
    Welcome To My Tool
    I hope you get even a little use out of it
    ENJOY:)
    
    insta:darsek_
    github:saleh-888
    ''')
welcom()

start = str(input("[*] Print <C> To Continue <E> To Exit: "))

if (start == "C"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3)

        host = input('[*] Enter The Host: ')
        port = int(input('[*] Enter The Port: '))

        def portscanner(port):
            if sock.connect_ex((host,port)):
                print('Port ',port,' is closed')

            else:
                print('Port ',port,' is open!')

        portscanner(port)
elif(start == "E"):
    print("THANK YOU FOR USING MY TooL:)")

else: 
    print('Just type the letters')
