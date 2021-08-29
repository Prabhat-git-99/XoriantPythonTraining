import Customer.Customer
import Customer.controllers.CustomerRegister

import shutil
columns = shutil.get_terminal_size().columns

from termcolor import colored

class CustomerRegister( Customer.Customer.Customer ):

    def __init__(self) -> None:
        super(CustomerRegister, self).__init__( '', '', '', '', '', '', '', '', '' )
        self.login =False
        self.password = ''
    
    
    def registerMenu( self ):
        print( 'Register Menu' )
        self.set_name( input( colored( 'Enter Name: ', 'blue' ) ) )
        self.set_address( input( colored( 'Enter Address: ', 'blue' ) ) )
        self.set_phone( input( colored( 'Enter Phone No.: ', 'blue' ) ) )
        self.set_email( input( colored( 'Enter Email: ', 'blue' ) ) )
        self.set_adhar( input( colored( 'Enter Aadhar No.: ', 'blue' ) ) )
        print( colored( '1. Saving Account', 'yellow' ).center( columns ) )
        print( colored( '2. Fixed Account', 'yellow' ).center( columns ) )
        account_type = int( input( colored( 'Which Type of account: ', 'blue' ) ) )
        obj = Customer.controllers.CustomerRegister.CustomerRegisteration( )
        # print('see ', self.getDetails( ) )
        obj.register( self.getDetails( ), account_type )
