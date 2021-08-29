from mysql.connector import cursor
import config

class CustomerService( ):

    def __init__(self) -> None:
        self.connect = config.DBConnect( )
        self.mydb = self.connect.get_mydb( )
        self.db_info = self.mydb.get_server_info
        if ( self.db_info ):
            print( 'Connected to Server', self.db_info )

    def __del__( self ):
        self.connect.close( )
        
    def customerLogin( self, accNo, password ):

        cursor = self.mydb.cursor( )
        query = 'SELECT * FROM customer WHERE accNo = %s'
        cursor.execute( query, ( accNo,) )
        # self.mydb.commit( )
        user = cursor.fetchone( )
        self.connect.set_cursor( cursor )

        query1 = 'SELECT * FROM account WHERE acc_no = %s'
        cursor.execute( query1, ( accNo,) )
        account = cursor.fetchone( )
        self.connect.set_cursor( cursor )
        return { 'user': user, 'account': account }

    def withdraw( self, query, accNo, amount ):
        print( 'inside withdrow')
        cursor = self.mydb.cursor( )
        print( accNo, amount )
        print( query, amount, accNo)
        cursor.execute( query, ( amount, accNo ) )
        self.mydb.commit( )
        found = cursor.fetchone( )
        self.connect.set_cursor( cursor )
        print('WIth ', found)
        return found
    
    def fetchBalance( self, query, accNo ):
        cursor = self.mydb.cursor( )
        cursor.execute( query, ( accNo,) )
        found = cursor.fetchone( )
        self.connect.set_cursor( cursor )
        return found

    def updateTransaction( self, query, accNo, to_acc_no, amount_transfered, date, trans_type, before_bal, updated_bal ):
        cursor = self.mydb.cursor( )
        cursor.execute( query, ( accNo, to_acc_no, amount_transfered, date, trans_type, before_bal, updated_bal ) )
        self.mydb.commit( )
        found = cursor.fetchall( )
        self.connect.set_cursor( cursor )
        # cursor.close( )
        return found

    def registerCustomer( self, info, query ):
        print( '**************' )
        a = 'requested'
        cursor = self.mydb.cursor( )
        cursor.execute( query, ( '', info[ 'name' ], info[ 'address' ], info[ 'phone' ], info[ 'email' ], info[ 'adhar' ], a ) )        
        self.mydb.commit( )
        found = cursor.fetchall( )
        self.connect.set_cursor( cursor )
        print( found )
