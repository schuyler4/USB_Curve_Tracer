import sys
from .interface import user_interface, init_serial

if __name__ == '__main__':
    if('software-test' in sys.argv):
        user_interface(None)
        exit()
    
    my_serial = init_serial()
    
    if(my_serial == None):
        exit()

    user_interface(my_serial)