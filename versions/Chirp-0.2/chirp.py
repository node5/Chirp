'Chirp, host a simple chat server. Written by Kale Champagnie <node5@github.com>'
from app import init
from app import start
from sys import argv
from sys import stdout
from sys import stdin
from sys import stderr



def main(args): 
    if (len(args) < 2):
        stderr.write('''
usage:
   chirp <command>

purpose:
   Chirp lets you host a simple chat server on your network. Once a user connects, they can choose to create or join a chat room.
   Users connect to your server via chirp clients such as, Eime. Clients are available to download from github.com/node5/Chirp/clients.

commands:
   init    create and configure your server
   start   start your server and allow people to join
''')
        
    elif (len(args) > 2):
        stderr.write('chirp: to many arguments were given')
          
    else:
        command = args[1]

        if (command == 'init'):
            init.main()

        elif (command == 'start'):
            start.main()
          
        else:
            stderr.write('chirp: unknown command')

main(argv)
