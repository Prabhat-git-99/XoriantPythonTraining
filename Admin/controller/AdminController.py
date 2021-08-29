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
