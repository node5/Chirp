from _thread import *
import socket
import json

 

class user(object):
    def __init__(self, name, connection):
        self.name = name
        self.connection = connection

            

class room(object):
    def __init__(self, name):
        self.name = name
        self.users = {}

    def accept(self, user):
        self.users[user.name] = user

        while (True):
            message = user.connection.recv(1024).decode('utf-8').strip()

            for name in self.users:
                _user = self.users[name]

                _user.connection.send(str.encode(user.name))
                _user.connection.send(str.encode(message))



class server(object):
    def __init__(self, name, port):
        self.name = name
        self.port = port
        self.rooms = {}
        self._socket = socket.socket()
    
    def listen(self):
        self._socket.bind(('', self.port))
        
        while (True):
            self._socket.listen(5)
            connection, address = self._socket.accept()
            start_new_thread(self.handle, (connection,))

    def handle(self, connection):
        name = connection.recv(1024).decode('utf-8').strip()
        _user = user(name, connection)
            
        while (True):
            action = connection.recv(1024).decode('utf-8').strip()

            if (action == 'create'):
                self.create(connection)
    
            elif (action == 'join'):
                self.join(_user, connection) 

            else:
                connection.send(str.encode('unknown command\n'))

    def create(self, connection): 
        name = connection.recv(1024).decode('utf-8').strip()
        _room = room(name)
        self.rooms[name] = _room

    def join(self, user, connection):
        name = connection.recv(1024).decode('utf-8').strip()
        _room = self.rooms[name]
        _room.accept(user)

        

def main():
    name = input('server name: ')
    
    file = open('save/servers/%s.json' % name)
    settings = json.load(file)

    name = settings['name']
    port = settings['port']
    
    _server = server(name, port)
    _server.listen()
    



        




            
