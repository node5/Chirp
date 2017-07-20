import argparse, json, socket, re;

from _thread import *;
      


class user(object): #

      def __init__(self, name, address, connection): #

            self.name = name;

            self.address = address;

            self.connection = connection;

      #

#



class room(object): #

      def __init__(self, name): #

            self.name = name;

            self.__users = {};

      #

      def accept(self, user): #

            self.__users[user.name] = user;

            while (True): #

                  message = user.connection.recv(1024).decode('utf-8')

                  for _user in self.__users.values(): #

                        _user.connection.send(str.encode('[%s] %s\n' % (user.name, message)))

                  #

            #

      #

      def remove(self, name): #

            self.__users.pop(name);

      #

#


      
class server(object): #

      def __init__(self): #

            self.settings = json.load(open('data/settings.json'));

            self.socket = socket.socket();

            self.__rooms = {};

            self.__users = {};

            self.listen();
            
      #

      def listen(self): #
      
            self.socket.bind((self.settings['host'], self.settings['port']));
            
            while (True): #

                  self.socket.listen(5);

                  connection, address = self.socket.accept();

                  start_new_thread(self.handle, (connection, address));

            #

      #

      def handle(self, connection, address): #
            
            connection.send(str.encode('your name: ')); # [-]
            
            user_name = connection.recv(1024).decode('utf-8').strip();

            self.__users[user_name] = user(user_name, address[0], connection);



            while (True): #
                  
                  connection.send(str.encode('action: ')); # [-]
                  
                  action = connection.recv(1024).decode('utf-8').strip();

                  if (action == 'create'): #
                        
                        connection.send(str.encode('room name: ')); # [-]
                        
                        room_name = connection.recv(1024).decode('utf-8');

                        self.__rooms[room_name] = room(room_name);

                  #

                  elif (action == 'join'): #
                        
                        connection.send(str.encode('room name: ')); # [-]
                        
                        room_name = connection.recv(1024).decode('utf-8');

                        self.__rooms[room_name].accept(self.__users[user_name]);    

                  #

                  elif (action == 'rooms'): #

                        for room_name in self.__rooms.keys(): #

                              connection.send(str.encode('%s\n' % (room_name)));
                              
                        #

                  #
      
                  else: #

                        connection.send(str.encode('error: unknown action %s\n' % (action)));

                  #

            #

      #

#



            
                        
      

            

