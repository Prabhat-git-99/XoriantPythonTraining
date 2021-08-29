import Customer.customerLogin
import Customer.customerRegister

import shutil
columns = shutil.get_terminal_size().columns

from termcolor import colored

class CustomerMenu(  ):

    def __init__(self ) -> None:
        self.accNo = ''
        self.password = ''
        self.printMenu( )

    
    def printMenu( self ):

        print( colored( 'Hello Customer!!', 'green', attrs = [ 'bold' ] ).center( columns ) )
        print( colored( '1. Login', 'magenta', attrs = [ 'bold' ] ).center( columns ) )
        print( colored( '2. Register', 'magenta', attrs = [ 'bold' ] ).center( columns ) )
        choice = int( input( colored( 'Enter your choice( 1-2 ): ', 'blue', attrs = [ 'bold' ] ) ) )
        if ( choice == 1 ):
            obj = Customer.customerLogin.CustomerLogin( )
            obj.loginMenu( )

        elif( choice == 2 ):
            obj = Customer.customerRegister.CustomerRegister( )
            obj.registerMenu( )

        else:
            print( colored( 'Thank You!', 'red', attrs=[ 'bold' ] ).center( columns ) )
        