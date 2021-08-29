import Customer.customerLogin
import Customer.customerRegister

class CustomerMenu(  ):

    def __init__(self ) -> None:
        self.accNo = ''
        self.password = ''
        self.printMenu( )

    
    def printMenu( self ):

        print( 'Hello Customer' )
        print( '1. Login' )
        print( '2. Register' )
        choice = int( input( 'Enter your choice( 1-2 ): ') )
        if ( choice == 1 ):
            obj = Customer.customerLogin.CustomerLogin( )
            obj.loginMenu( )

        elif( choice == 2 ):
            obj = Customer.customerRegister.CustomerRegister( )
            obj.registerMenu( )

        else:
            print('bye')