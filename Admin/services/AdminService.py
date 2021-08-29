from mysql.connector import cursor
import config

class AdminService( ):

    def __init__( self ) -> None:
        self.connect = config.DBConnect( )
        self.mydb = self.connect.get_mydb( )
        self.db_info = self.mydb.get_server_info
        # if ( self.db_info ):
            # print( 'Connected To Server', self.db_info )

    def adminLogin( self, name, password ):

        print( password )
        cursor = self.mydb.cursor( )
        query = 'SELECT * FROM admin WHERE admin_name = %s'
        cursor.execute( query, ( name,) )
        found = cursor.fetchone( )
        self.connect.set_cursor( cursor )
        return found
    
    def fetchAllCustomer( self ):
        query = 'select * from customer'
        cursor = self.mydb.cursor( )
        cursor.execute( query )
        found = cursor.fetchall( )
        self.connect.set_cursor( cursor )
        return found
        
    def fetchSingleCustomer( self, id ):
        cursor = self.mydb.cursor( )
        query = 'select * from customer where accNo = %s'
        cursor.execute( query, ( id,) )
        found = cursor.fetchone( )
        self.connect.set_cursor( cursor )
        return found
    
    def fetchByCID( self, id ):
        cursor = self.mydb.cursor( )
        query = 'select * from customer where customer_id = %s'
        cursor.execute( query, ( id,) )
        found = cursor.fetchone( )
        self.connect.set_cursor( cursor )
        return found
    
    def verifyCustomer( self, id, accNo, pin ):
        cursor = self.mydb.cursor( )
        # print( 'updating' )
        query = 'update customer set accNo=%s, status="1" where customer_id = %s'
        cursor.execute( query, ( accNo,id ) )
        self.mydb.commit( )
        cursor.fetchone( )
        self.connect.set_cursor( cursor )
        # print( found )
        # return found
    
    def openAccount( self, query, query1, accNo, pin ):
        cursor = self.mydb.cursor( )
        cursor.execute( query, ( accNo, ) )
        self.mydb.commit( )
        # found = cursor.fetchone( )
        self.connect.set_cursor( cursor )
        cursor = self.mydb.cursor( )
        cursor.execute( query1, ( pin, accNo ) )
        self.mydb.commit( )
        # found = cursor.fetchone( )
        self.connect.set_cursor( cursor )
        # return found

    
    def deleteByAcc( self, accNo ):
        cursor = self.mydb.cursor( )
        query = 'delete from customer where accNo = %s'
        cursor.execute( query, ( accNo,) )
        self.mydb.commit( )
        # found = cursor.fetchone( )
        self.connect.set_cursor( cursor )
        return 'success'

    def checkTransaction( self, accNo ):

        
        query = 'select * from transaction where accNo = %s'
        cursor = self.mydb.cursor( )
        cursor.execute( query, ( accNo, ) )
        found = cursor.fetchall( )
        self.connect.set_cursor( cursor )
        return found