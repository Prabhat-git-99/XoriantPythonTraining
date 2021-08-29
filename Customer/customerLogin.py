import Customer.Customer
import Customer.controllers.CustomerController

class CustomerLogin( Customer.Customer.Customer ):

    def __init__( self ):
        super(CustomerLogin, self).__init__( '', '', '', '', '', '', '', '', '' )
        self.login =False
        self.password = ''

    def loginMenu( self ):
        print('menu login')
        accNo = input( 'Enter Account No.: ' )
        self.password = input( 'Enter 4 Digit PIN: ' )
        obj = Customer.controllers.CustomerController.CustomerController( accNo, self.password )
        found = obj.customerLogin( )
        if found[ 'status' ] == 'not found':
            print( 'Wrong Credentials!' )
        else:
            print( 'Welcome' )
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
        print( details )


    def menu( self ):

        if self.login:
            flag = True
            while flag:

                print( '******HELLO CUSTOMER*******' )
                print( '1. Withdraw' )
                print( '2. Deposit' )
                print( '3. Money Transfer' )
                print( '4. Balance Enquiry' )
                print( '5. Reset PIN' )
                print( '6. Edit Details' )
                print( '7. Exit' )
                inp = int( input( 'Enter Your Choice( 1-7 ): ' ) )

                if inp == 7:
                    flag = False
                    break
        
                else:
                    if inp == 1:
                        print( '1. Saving' ) if self.saving_acc == 'approved' else 'Saving account is not approved yet!'
                        print( '2. Fixed' ) if self.fixed_acc == 'approved' else 'Fixed account is not approved yet!'
                        op = int( input( 'Enter Type of Account: ') )
                        if op == 1:
                            obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                            obj.withdraw( 'saving', self.saving_acc )
                        elif op == 2:
                            obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                            obj.withdraw( 'fixed', self.fixed_acc)

                    elif inp == 2:
                        print( '1. Saving' ) if self.saving_acc == 'approved' else 'Saving account is not approved yet!'
                        print( '2. Fixed' ) if self.fixed_acc == 'approved' else 'Fixed account is not approved yet!'
                        op = int( input( 'Enter Type of Account: ') )
                        if op == 1:
                            obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                            obj.deposit( 'saving', self.saving_acc )
                        elif op == 2:
                            obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                            obj.deposit( 'fixed', self.fixed_acc )

                    elif inp == 3:
                        to_acc = input( 'Enter Account no. to transfer: ' )
                        # print( '1. Saving' ) if self.saving_acc == 'approved' else 'Saving account is not approved yet!'
                        # print( '2. Fixed' ) if self.fixed_acc == 'approved' else 'Fixed account is not approved yet!'
                        obj = Customer.controllers.CustomerController.CustomerController( self.accNo, self.password )
                        obj.transferMoney( to_acc )

                    elif inp == 4:
                        pass

                    elif inp == 5:
                        pass

                    elif inp == 6:
                        pass

