import mysql.connector
from mysql.connector import Error
from termcolor import colored
import shutil
columns = shutil.get_terminal_size().columns

host = 'localhost'
database = 'xorpy' 
user='root' 
password='Prabhat@9999'

class DBConnect():

    def __init__(self) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.mydb = ''
        self.cursor = ''
        self.start()

    def start( self ):

        self.mydb = mysql.connector.connect( host = self.host, database = self.database, user= self.user, password= self.password  )
        try:
            if self.mydb.is_connected():
                db_info = self.mydb.get_server_info
        except Error as e:
                print('Error')
        
    def get_mydb( self ):
        return self.mydb

    def set_cursor( self, cursor ):
        self.cursor = cursor

    def close( self ):
        
        if self.mydb.is_connected( ):
            self.cursor.close( )
            self.mydb.close( )
            print( colored( 'MySQL connection is closed ', 'red' ).center( columns ) )

    print( colored( '***************************************************************************', 'red' ).center( columns ) )
