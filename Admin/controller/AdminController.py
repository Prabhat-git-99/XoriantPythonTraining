from datetime import datetime
from re import A
import config
import Admin.services.AdminService

import shutil
from termcolor import colored
columns = shutil.get_terminal_size().columns

class AdminController():

    def __init__( self, name, password ):
        self.name = name
        self.password = password
        # return self.adminLogin()
        self.obj = Admin.services.AdminService.AdminService( )

    def adminLogin( self ):

        found = self.obj.adminLogin( self.name, self.password )
        if ( found ):
            # print( found )
            if ( found[2] == self.password ):
                return True
        else:
            return False
    
    def fetchAllCustomer( self ):

        found = self.obj.fetchAllCustomer( )
        return found
    
    def fetchSingleCustomer( self, id ):

        found = self.obj.fetchSingleCustomer( id )
        return found

    def verifyCustomer( self ):

        cid = int( input( colored( 'Enter Customer ID: ', 'blue', attrs = [ 'bold' ] ) ) )
        
        found = self.obj.fetchByCID( cid )
        
        if ( found[ 7 ] == 1 and ( found[ 8 ] == 'approved' and found[ 9 ] == 'approved' ) ):
            print( colored( 'Customer is already Verified', 'red', attrs = [ 'bold' ] ).center( columns ) )
        else:
            if ( found[ 8 ] != 'approved' and found[ 9 ] != 'approved' ):
                accNo = input( colored( 'Assign unique account number: ', 'blue', attrs = [ 'bold' ] ) )
                pin = input( colored( 'Assign 4 digit pin: ', 'blue', attrs = [ 'bold' ] ) )
                self.obj.verifyCustomer( cid, accNo, pin )
                # print( found )
                self.openAccount( found, accNo, pin )
            else:
                accNo = found[ 1 ]
                pin = input( colored( 'Assign New 4 digit pin: ', 'blue', attrs = [ 'bold' ] ) )
                self.obj.verifyCustomer( cid, accNo, pin )
                self.openAccount( found, accNo, pin )

        
    def openAccount( self, found, accNo, pin ):

        if found[ 8 ] == 'requested':
            query = 'update customer set saving_acc="approved" where accNo=%s'
            if found[ 9 ] == 'approved':
                query1 = 'update account set balance_saving=0, pin=%s where acc_no=%s'
            else:
                query1 = 'insert into account ( balance_saving, pin, acc_no) values (0, %s, %s)'
            self.obj.openAccount( query, query1, accNo, pin )


        elif found[ 9 ] == 'requested':
            query = 'update customer set fixed_acc="approved" where accNo=%s'
            if found[ 8 ] == 'approved':
                query1 = 'update account set balance_fixed=0, pin=%s where acc_no=%s'
            else:
                query1 = 'insert into account ( balance_fixed, pin, acc_no ) values (0, %s, %s)'
            self.obj.openAccount( query, query1, accNo, pin )


    
    def deleteCustomer( self ):

        accNo = input( colored( 'Enter Account No: ', 'blue', attrs = [ 'bold' ] ) )
        res = self.obj.deleteByAcc( accNo )

    def checkTransaction( self, acc ):

        res = self.obj.checkTransaction( acc )
        for row in res:
            print( '************************' )
            print( colored( 'Account Number : ', 'blue', attrs = [ 'bold' ] ), row[ 0 ] )
            print( colored( 'To : ', 'blue', attrs = [ 'bold' ] ), row[ 1 ] )
            print( colored( 'Amount Transfered : ', 'blue', attrs = [ 'bold' ] ), row[ 2 ] )
            print( colored( 'Date : ', 'blue', attrs = [ 'bold' ] ), row[ 3 ] )
            print( colored( 'Transaction Type : ', 'blue', attrs = [ 'bold' ] ), row[ 4 ] )
            print( colored( 'Previous Balance : ', 'blue', attrs = [ 'bold' ] ), row[ 5 ] )
            print( colored( 'Updated Balance : ', 'blue', attrs = [ 'bold' ] ), row[ 6 ] )

    def initiateInterest( self ):

        cid = int( input( colored( 'Enter Customer ID: ', 'blue', attrs = [ 'bold' ] ) ) )
        
        found = self.obj.fetchByCID( cid )
        bal = self.obj.checkBalance( found[ 1 ] )
        print( found, bal )
        try:
            print( found[ 8 ] , found[ 8 ] == 'approved' )
            if ( found[ 8 ] == 'approved' ):
                print('1', found[ 8 ] , found[ 8 ] == 'approved' )
                saving_bal = bal[ 0 ][ 1 ]
                date = found[ 10 ]
                currentDate = datetime.now( )
                print( date, currentDate, saving_bal )
                diff = ( currentDate - date ).total_seconds( )
                mins = diff/60
                hours = mins/60
                days = hours/24
                month = days/30
                if month >= 1:
                    interest = 0.06*int( saving_bal )
                    print( interest, found[ 1 ] )
                    total = int( saving_bal ) + interest
                    print( total )
                    self.obj.sendDeposit( int( found[ 1 ] ), 1 , str( total ) )

                else:
                    print( colored( 'Interested will be calculated after completion of 30 Days', 'yellow', attrs = [ 'bold' ] ).center( columns ) )

            else:
                print( colored( 'Saving Account is not approved yet!', 'red', attrs = [ 'bold' ] ).center( columns ) )


        except:
            print( colored( 'NO BALANCE', 'red', attrs = [ 'bold' ] ).center( columns ) )
        

        try:

            if ( found[ 9 ] == 'approved' ):
                date = found[ 11 ]
                fixed_bal = bal[ 0 ][ 2 ]
                currentDate = datetime.now( )
                diff = ( currentDate - date ).total_seconds( )
                mins = diff/60
                hours = mins/60
                days = hours/24
                month = days/30
                if month >= 1:
                    interest = 0.08*int( fixed_bal )
                    print( interest, found[ 1 ] )
                    total = int( fixed_bal ) + interest
                    self.obj.sendDeposit( int( found[ 1 ] ), 2 , str( total ) )        
                else:
                    print( colored( 'Interested will be calculated after completion of 30 Days', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
            else:
                print( colored( 'Fixed Account is not approved yet!', 'red', attrs = [ 'bold' ] ).center( columns ) )

        
        except:

            print( colored( 'NO BALANCE', 'red', attrs = [ 'bold' ] ).center( columns ) )
            
