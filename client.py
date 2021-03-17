# -*- coding: utf-8 -*-

import socket
import threading
import sys
import ipaddress
from bot import *
import re

exit_commando = ["disconnect-server", "quit-server"]

if len(sys.argv) == 2:
    arg = (sys.argv[1])
    arg = arg.lower()
    print(arg)
    if arg == '-h' or arg == 'help':
        print("\n-- WELCOME TO THE CLIENT CONNECTION -- \n\n Follow these steps to connect to the server: \n 1."
              "In the terminal-window, your input needs to be \n --> python [script-name] [host (IP-address)] ["
              "port-number]\n You have to make sure that both your host- and port-number is valid and "
              "of digits. This input must match \nthe already connected server."
              " If the input is correct, your client-connection should be established\n"
              "and connected to the server.\n")
        exit()
elif len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
else:
    # Checking legal input parameters
    # Connection Data
    try:
        IP = ipaddress.ip_address(sys.argv[1])
    except ValueError:
        print("Address/netmask is invalid. Try again.")
        exit()
    if sys.argv[2].isdigit() is False:
        print("Your input for port must be an integer. Please try again.")
        exit()

# Input parameters are valid
HOST = sys.argv[1]
PORT = int(sys.argv[2])

# Choose nickname
nickname = input("Choose your nickname: ")

# Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


# Listening to server and sending nickname
def receive():
    while True:
        try:
            # Receive message from server
            # if 'NICK' send nickname
            message = client.recv(1024).decode('utf-8')
            if message == 'USER':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Close connection when error
            print("An error occurred!")
            client.close()
            break


# Sending messages to server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        if message:
            print(message)
            message = message.encode('utf-8')
            message_test = '{}: {}'.format(nickname, conversation(format(nickname)))
            client.send(message)


# Threads for receiving and wiritng messages to the server
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()