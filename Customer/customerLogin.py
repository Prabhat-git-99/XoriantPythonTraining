import Customer.Customer
import Customer.controllers.CustomerController

import shutil
columns = shutil.get_terminal_size().columns

from termcolor import HIGHLIGHTS, colored

class CustomerLogin( Customer.Customer.Customer ):

    def __init__( self ):
        super(CustomerLogin, self).__init__( '', '', '', '', '', '', '', '', '' )
        self.login =False
        self.password = ''

    def loginMenu( self ):
        accNo = input( colored( 'Enter Account No.: ', 'blue', attrs = [ 'bold' ] ) )
        self.password = input( colored( 'Enter 4 Digit Pin: ', 'blue', attrs = [ 'bold' ] ) )
        obj = Customer.controllers.CustomerController.CustomerController( accNo, self.password )
        found = obj.customerLogin( )
        if found[ 'status' ] == 'not found':
            print( colored( 'Wrong Credentials!', 'red', attrs = [ 'bold' ] ).center( ) )
        else:
            print( colored( 'Welcome', 'green', attrs = [ 'bold' ] ).center( columns ) )
            self.login = True
            self.set_acc( found[ 'user' ][ 1 ] )
            self.set_name( found[ 'user' ][ 2 ] )
            self.set_address( found[ 'user' ][ 3 ] )
            self.set_phone( found[ 'user' ][ 4 ] )
            self.set_email( found[ 'user' ][ 5 ] )
            self.set_adhar( found[ 'user' ][ 6 ] )
            self.set_status( found[ 'user' ][ 7 ] )
            self.set_saving( found[ 'user' ][ 8 ] )
            self.set_fixed( found[ 'user' ][ 9 ] )
            self.showCustomerDetail( )
            self.menu( )


    def showCustomerDetail( self ):
        # details = Customer.Customer.Customer.getDetails( )
        details = self.getDetails( )
        print( '' )
        print( colored( 'Hello ' + details[ 'name' ] , 'cyan', attrs = [ 'bold' ] ).center( columns ) )


    def menu( self ):

        if self.login:
            flag = True
            while flag:

                print( colored( '******HELLO CUSTOMER*******', 'grey', attrs = [ 'bold' ] ).center( columns ) )
                print( colored( '1. Withdraw', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
                print( colored( '2. Deposit', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
                print( colored( '3. Money Transfer', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
                print( colored( '4. Balance Enquiry', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
                print( colored( '5. Reset PIN', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
                # print( '6. Edit Details' )
                print( colored( '6. Exit', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
                inp = int( input( colored( 'Enter Your Choice( 1-6 ): ', 'blue', attrs = [ 'bold' ] ) ) )

                if inp == 7:
                    flag = False
                    break
        
                else:
                    if inp == 1:
                        print( colored( '1. Saving', 'yellow', attrs = [ 'bold' ] ).center( columns ) ) if self.saving_acc == 'approved' else print( colored( 'Saving account is not approved yet!', 'red' ) )
                        print( colored( '2. Fixed', 'yellow', attrs = [ 'bold' ] ).center( columns ) ) if self.fixed_acc == 'approved' else print( colored( 'Fixed account is not approved yet!', 'red' ) )
                        op = int( input( colored( 'Enter Type of Account: ', 'blue', attrs = [ 'bold' ] ).center( columns ) ) )
                        if op == 1:
                            obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                            obj.withdraw( 'saving', self.saving_acc )
                        elif op == 2:
                            obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                            obj.withdraw( 'fixed', self.fixed_acc)

                    elif inp == 2:
                        print( colored( '1. Saving', 'yellow', attrs = [ 'yellow' ] ).center( columns ) ) if self.saving_acc == 'approved' else 'Saving account is not approved yet!'
                        print( colored( '2. Fixed', 'yellow', attrs = [ 'yellow' ] ).center( columns ) ) if self.fixed_acc == 'approved' else 'Fixed account is not approved yet!'
                        op = int( input( colored( 'Enter Type of Account: ', 'blue', attrs = [ 'bold' ] ).center( columns ) ) )
                        if op == 1:
                            obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                            obj.deposit( 'saving', self.saving_acc )
                        elif op == 2:
                            obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                            obj.deposit( 'fixed', self.fixed_acc )

                    elif inp == 3:
                        to_acc = input( colored( 'Enter Account no. to transfer: ', 'blue', attrs = [ 'bold' ] ) )
                        obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                        obj.transferMoney( to_acc )

                    elif inp == 4:

                        obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                        obj.balanceEnquiry( )

                    elif inp == 5:
                        obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                        obj.resetPin( )

                    elif inp == 6:
                        return

