import Customer.Customer
import Customer.controllers.CustomerRegister

class CustomerRegister( Customer.Customer.Customer ):

    def __init__(self) -> None:
        super(CustomerRegister, self).__init__( '', '', '', '', '', '', '', '', '' )
        self.login =False
        self.password = ''
    
    
    def registerMenu( self ):
        print( 'Register Menu' )
        self.set_name( input( 'Enter Name: ' ) )
        self.set_address( input( 'Enter Address: ' ) )
        self.set_phone( input( 'Enter Phone No.: ' ) )
        self.set_email( input( 'Enter Email: ' ) )
        self.set_adhar( input( 'Enter Aadhar No.: ' ) )
        print( '1. Saving Account' ) 
        print( '2. Fixed Account' )
        account_type = int( input( 'Which Type of account: ' ) )
        obj = Customer.controllers.CustomerRegister.CustomerRegisteration( )
        print('see ', self.getDetails( ) )
        obj.register( self.getDetails( ), account_type )
