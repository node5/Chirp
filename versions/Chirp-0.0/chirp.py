'Chirp, host your own chat server. Written by Kale Champagnie <node5@github.com>'
from sys import argv
from app import create
from app import start
from app import change
from app import list
from app import delete



def main(args): 
    if (len(args) < 2):
        print('''
usage:
   chirp <command>

purpose:
   Chirp lets you host chat servers on your network. Once a user connects, they can choose to create or join a room.
   Users connect to your server via chirp clients such as Eime. Clients are available to download from github.com/node5/Chirp/clients.

commands:
   create   create a new server
   start    start a server, allow clients to connect      
   change   change a server's settings
   list     list existing servers
   delete   delete a server
   
author:
   Kale Champagnie <node5@github.com>
''')
        
    elif (len(args) > 2):
        print('chirp: to many arguments were given')
          
    else:
        command = args[1]

        if (command == 'create'):
            create.main()

        elif (command == 'start'):
            start.main()

        elif (command == 'change'):
            change.main()

        elif (command == 'list'):
            list.main()

        elif (command == 'delete'):
            delete.main()
          
        else:
            print('chirp: unknown command')

main(argv)
