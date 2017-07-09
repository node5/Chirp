import argparse;



def main(): #

      parser = argparse.ArgumentParser(usage='''chirp <command>

Chirp is an app that lets you host your own chat server. Other users can connect to your server using a Chirp client.
To download a client to can visit https://github.com/node5/Chirp/clients

''');

      parser.add_argument('command', type=str, help='command which Chirp will execute');

      arguments = parser.parse_args();

      
#

main();
