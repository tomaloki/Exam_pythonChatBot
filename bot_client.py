# -*- coding: utf-8 -*-

import socket
import threading
import random
import sys
import ipaddress
from bot import *
import time
import select
import re

bot_nicknames = ["AnnaBot", "DerekBot", "PetronellaBot", "JuanBot"]
used_words = []
# Connection data

if len(sys.argv) == 2:
    arg = (sys.argv[1])
    arg = arg.lower()
    print(arg)
    if arg == '-h' or arg == 'help':
        print("\n-- WELCOME TO THE BOT-CLIENT CONNECTION -- \n\n Follow these steps to connect to the server: \n 1."
              "In the terminal-window, your input needs to be \n --> python [script-name] [host (IP-address)] ["
              "port-number] [name-of-bot] \n You have to make sure that both your host- and port-number is valid and "
              "of digits. This input must match \nthe already connected server. Your bot-input must be one of the"
              " the following: AnnaBot, PetronellaBot, JuanBot, DerekBot. \nThese names must be typed in with the same"
              " upper- and lowercase characters.\n"
              "If the input is correct, your bot-client should be able to with the server.\n")
    exit()
elif len(sys.argv) != 4:
    print("Correct usage: script, IP address, port number, bot")
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
        # Check if input-bot is in list over bots
    try:
        if sys.argv[3] not in bot_nicknames:
            print("Yo have to enter a valid bot.")
            exit()
    except ValueError:
        print("An error has occurred")
        exit()

# Input parameters are valid
HOST = sys.argv[1]
PORT = int(sys.argv[2])
BOT = sys.argv[3]

# Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, int(PORT)))


# Listening to the server
def receive():
    while True:
        # Receive message from server
        # For received "USER"-request, send the username in return
        message = client.recv(1024).decode('utf-8')
        try:
            if message == 'USER':
                client.send(BOT.encode('utf-8'))
            else:
                print(f"{message}")

        except:
            print("An error occurred!")
            client.close()
            break
        for word in sayings:
            if word in re.split('[ ?.,!]', message):
                if word in used_words:
                    bot_message = '{}: {}'.format(BOT, conversation(format(word)))
                    time.sleep(2)
                    client.send(bot_message.encode('utf-8'))
                    print(bot_message)
                    break
                if BOT == "AnnaBot":
                    bot_message = '{}: {}'.format(BOT, anna(format(word)))
                    time.sleep(3)
                    client.send(bot_message.encode('utf-8'))
                    print(bot_message)
                    used_words.append(word)
                elif BOT == "DerekBot":
                    bot_message = '{}: {}'.format(BOT, derek(format(word)))
                    time.sleep(4)
                    client.send(bot_message.encode('utf-8'))
                    print(bot_message)
                    used_words.append(word)
                elif BOT == "PetronellaBot":
                    bot_message = '{}: {}'.format(BOT, petronella(format(word)))
                    time.sleep(5)
                    client.send(bot_message.encode('utf-8'))
                    print(bot_message)
                    used_words.append(word)
                elif BOT == "JuanBot":
                    bot_message = '{}: {}'.format(BOT, juan(format(word)))
                    time.sleep(6)
                    client.send(bot_message.encode('utf-8'))
                    print(bot_message)
                    used_words.append(word)
                else:
                    print("An error has occurred.")
                break


receive()
