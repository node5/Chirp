from json import dump
from socket import gethostbyname
from socket import gethostname


        
def main():
    with open('data/settings.json', 'w+') as file:
        settings = {
            'your name': '',
            'server name': '',
            'server ip': gethostbyname(gethostname()),
            'server port': 63521
        }

        for key in settings:
            while (not settings[key]):
                settings[key] = input('( %s )\n' % key)

        dump(settings, file)

    print('your server was successfully created') 
        

        



            

        
                
                
        
        
        


