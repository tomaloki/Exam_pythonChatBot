## Information about the code ##


This assignment is written in Python, and the python-version that has been used while testing and running is
Python 3.9.2.

In addition to the requested files, client.py and server.py, I have chosen to add two more files:
- bot_client.py
- bot.py


I have chosen to give the client the possibility to log in either as a bot or as a human. Therefore, I have divided the
client-file in two - client.py, where you connect as a "human" and bot_client.py, where you connect as a bot.
bot_client.py has some differences in the code, for example you can not communicate via the command line when you
are connected via the bot_client.py-file. This is possible when you connect the client.py.

The file called *bot.py* contains all the information which gives each bot its personality. This is imported
in each of the other files.

------
** INPUT PARAMETERS **
All of the python-files have input parameters:
- server.py
    --> The input should be python [server.py] [HOST] [PORT]
    --> For example python server.py 127.0.0.1 5050

- client.py
    --> The input should be python [client.py] [HOST] [PORT]
    --> For example python server.py 127.0.0.1 5050


- bot_client.py
    --> The input should be python [client.py] [HOST] [PORT] [BOT-NAME]
    --> The list of bots you can connect as is the following: AnnaBot, PetronellaBot, DerekBot, JuanBot
    --> For example python client.py 127.0.0.1 5050 AnnaBot
----

NB!
The input parameters which concern host and port must be the same for server.py,
client.py and bot_client.py.

** EXAMPLES OF CONVERSATION WITH BOT **
You have the option to chat with the bot(s) as a connected client or via the server. You can connect
multiple clients and disconnect whenever you feel like it. The words that the bots respond to are the
same for the server-input and the client-input.

A full list of all of the words the bots respond to:
sayings = ["work", "play", "eat", "cry", "sleep", "fight", "hello", "Hey", "yo", "wind", "rain", "snow", "sunshine",
           "pretty", "kind", "beautiful", "intelligent", "wise", "name"]
All of the bots might not respond to all of the words.


It is advised to use one word at a time. The chosen word can be anywhere in the sentence you choose to send.

In the server.py file there is a variable called LIMIT - this is currently set to 4, but this can be
changed. The notification you get when clients and bots are connecting and disconnecting is made with
LIMIT = 4 connections in mind.

If you are in the "talking-loop" with the bots and clients from the server, you can either write "quit" or
a word that is not in the list of words that the bots respond to, to exit the loop. From here other clients
can connect and the bots can also disconnect again.

NB!
While in the "talking-loop" with the bots, other clients can sign in - but they will not be accepted by the server
until the "talking-loop" has ended.
To notify: if you choose to connect 4 ordinary client.py's, the loop in the server will start.

