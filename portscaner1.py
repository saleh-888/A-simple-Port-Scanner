#!/usr/bin/python
import socket 

def welcome():
    print('''
    HI And Welcome To My Scanning Tool 
    I Hope YOU ENJOY:)
   
   insta:darsek_
    ''')
    
welcome()
parameter = str(input("Press C to Continue Press E to Exit: "))
if (parameter == "C"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = input("Enter The IP Adress: ")
    port = int(input("Enter The PORT Number: "))

    def portscanner(port):
        if sock.connect_ex((host,port)):
            print("Port ",port," is closed")

        else:
            print("Port ",port," is opend!")

    portscanner(port)

elif(parameter == "E"):
    print("I hope yOu EnJoY:)")
