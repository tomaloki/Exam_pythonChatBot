# -*- coding: utf-8 -*-

import socket
import sys
import re
import select
import ipaddress
from bot import *
import time
import re

# Lists for clients, bots and their nicknames


clients = []
nicknames = []
bot_nicknames = ["AnnaBot", "DerekBot", "PetronellaBot", "JuanBot"]
count = 0

# Handling input parameters in the terminal window.

if len(sys.argv) == 2:
    arg = (sys.argv[1])
    arg = arg.lower()
    if arg == '-h' or arg == 'help':
        print("\n-- WELCOME TO THE SOCKET-SERVER -- \n\n Follow these steps to connect to the server: \n 1."
              "In the terminal-window, your input needs to be \n --> python [script-name] [host (IP-address)] ["
              "port-number] \n You have to make sure that both your host- and port-number is valid and of digits. If "
              "the \n input is correct, your server should be up and running. \n You can then connect your preferred"
              " client-connection, whether it is a human client or a bot.  \n")
    else:
        print("If you need help or more information on how to run the server, type '-h' or 'help' after 'server.py'"
              "\nin the command line.")
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


def get_listening_socket():
    print("Server is running and looking for connections...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setblocking(True)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, int(PORT)))
    print(f"Server socket bound with IP: {HOST} and IP: {PORT}")
    server_socket.listen(0)
    return server_socket


connected_socket = get_listening_socket()
# Defining a limit of connections, which can be de- or increased.
LIMIT = 4
# List of connected sockets
client_connections = {connected_socket}


# Sending message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Handling incoming messages to the server
def receive():
    global count
    while True:
        read_socket, write_socket, exception_socket = select.select(client_connections, [], [])
        # if connected_socket is in read_socket --> we have a new connection on the listening socket
        for notified_socket in read_socket:
            if notified_socket == connected_socket:
                client_socket, client_address = connected_socket.accept()
                print("Connected with {}".format(str(client_address)))

                # Request nickname from connection and store it
                client_socket.send('USER'.encode('utf-8'))
                nickname = client_socket.recv(1024).decode('utf-8')

                client_connections.add(client_socket)
                nicknames.append(nickname)
                count = count + 1
                clients.append(client_socket)

                # Printing and broadcasting the new connection to the rest of the connections
                print("-- Nickname is {} --".format(nickname))
                broadcast("{} joined the server.".format(nickname).encode('utf-8'))
                client_socket.send('\nYou are connected to the server!'.encode('utf-8'))

                if len(client_connections) > LIMIT:  # ">, bigger than" because connected_socket is also in this list
                    # Access is denied for user, but this will not happen in this scenario because when the
                    # "talking-loop" is done, the server is open for new connections again.
                    client_connections.remove(connected_socket)
                    connected_socket.close()

                elif len(client_connections) < LIMIT:
                    print(
                        "\n-- READ: If you want to be able to communicate with connected bots from the server, \nplease"
                        " connect minimum 1 or maximum 4 bots. You need to fill the 'empty' \nspots with"
                        " other clients if you don't want to use 4 bots. --\n")
                    if count == 1:
                        print(f"We now have {count} connection, waiting for {LIMIT - (count + 1)} more!")
                    else:
                        print(f"We now have {count} connections, waiting for {LIMIT - (count + 1)} more!")
                elif len(client_connections) == LIMIT:
                    start_message = f"How wonderful, we have reached the limit of {count} connections -" \
                                    f"Let's start!"
                    print(start_message)
                    for _ in client_connections:
                        time.sleep(3)
                        word = input("Let's give the bots a suggestion: ")
                        if word == 'quit':
                            break
                        elif word not in sayings:
                            break
                        else:
                            print(f"Me: Do you guys want to {format(word)}?")
                            broadcast(f"Me: Do you guys want to {format(word)}?".encode('utf-8'))
                            for client in clients:
                                answer = client.recv(1024).decode("utf-8")
                                for bot_client in clients:
                                    if bot_client == client:
                                        continue
                                    bot_client.send(answer.encode("utf-8"))
                                print(f"Received message: {answer}")

            else:  # Else - we read from an already established connection
                data = notified_socket.recv(1024).decode("utf-8")
                print(f"Received message: " + str(data))

                if not data:
                    index = clients.index(notified_socket)
                    client_connections.remove(notified_socket)
                    clients.remove(notified_socket)
                    notified_socket.close()
                    nickname = nicknames[index]
                    disconnect_message = f"{nickname} has disconnected from the server"
                    print(disconnect_message)
                    broadcast(disconnect_message.encode('utf-8'))
                    count = count - 1
                    print("Number of connections on the server: {}".format(count))
                    nicknames.remove(nickname)

                # Forwarding message to client(s)
                for client in clients:
                    try:
                        # Making sure that it does not go back to sender
                        if client == notified_socket:
                            continue
                        client.sendall(data.encode("utf-8"))

                    except:
                        print("An error has occurred.")
                        sys.exit()


if __name__ == "__main__":
    receive()
