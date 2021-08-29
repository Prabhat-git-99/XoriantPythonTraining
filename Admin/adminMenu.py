# from BankingProj.Admin.services.AdminService import AdminService
from typing import Container
from mysql import connector
import Admin.services.AdminService
import Admin.controller.AdminController

import shutil
from termcolor import colored
columns = shutil.get_terminal_size().columns

class AdminMenu():

    def __init__(self) -> None:
        self.name = ''
        self.password = ''
        self.printMenu()


    def showFeedBack( self, msg ):
        print(msg)

    def printMenu( self ):

        print( colored( 'ADMIN PANEL', 'green', attrs = [ 'bold' ] ).center( columns ) )
        flag = True
        self.name = input( colored( 'Enter Name: ', 'blue', attrs = [ 'bold' ] ).center( columns ) )
        self.password = input( colored( 'Enter Password: ', 'blue', attrs = [ 'bold' ] ).center( columns ) )
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        login_status = obj.adminLogin()
        
        while flag:
            
            if login_status:
                choice = self.menu()
                if choice == 6:
                    flag = False
                    break
                elif choice == 1:
                    self.fetchAllCustomer()
                elif choice == 2:
                    self.fetchById()
                elif choice == 3:
                    self.verifyCustomer()
                elif choice == 4:
                    self.deleteCustomer()
                elif choice == 5:
                    self.checkTransaction()
            else:
                print( colored( 'Please enter correct credentials!', 'red', attrs = [ 'bold' ] ).center( columns ) )
                flag = False
                break

    def checkTransaction(self):
        # self.fetchAllCustomer( )
        acc_no = input( colored( 'Enter Account Number: ', 'blue', attrs = [ 'bold' ] ) )
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.checkTransaction( acc_no )
        print( records )

    def deleteCustomer(self):
        print( colored( 'Which customer you want to delete ', 'magenta', attrs = [ 'bold' ] ).center( columns ) )
        self.fetchAllCustomer( )
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.deleteCustomer( )

    def verifyCustomer(self):
        print( colored( 'Which customer you want to verify ', 'magenta', attrs = [ 'bold' ] ).center( columns ) )
        self.fetchAllCustomer( )
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.verifyCustomer( )


    def fetchById(self):
        id = int(input( colored( 'Enter Account No. :', 'blue', attrs = [ 'bold' ] ) ) )
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.fetchSingleCustomer( id )
        self.printRecord( records )
    
    def fetchAllCustomer(self):
        print( colored( 'All Customers', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.fetchAllCustomer(  )
        for row in records:
            self.printRecord( row )
                    
    def printRecord( self, row ):
        print( colored( '*********************************************', 'white', attrs = [ 'bold' ] ).center( columns ) )
        print( colored( 'CustomerId : ', 'blue', attrs = [ 'bold' ] ), row[0])
        print( colored( 'Account Num : ', 'blue', attrs = [ 'bold' ] ), row[1])
        print( colored( 'Name : ', 'blue', attrs = [ 'bold' ] ), row[2])
        print( colored( 'Address : ', 'blue', attrs = [ 'bold' ] ), row[3])
        print( colored( 'Mobile : ', 'blue', attrs = [ 'bold' ] ), row[4])
        print( colored( 'Email : ', 'blue', attrs = [ 'bold' ] ), row[5])
        print( colored( 'Aadhar : ', 'blue', attrs = [ 'bold' ] ), row[6])
        print( colored( 'Status( 1-Verified 2-Not Verified ) : ', 'blue', attrs = [ 'bold' ] ), row[7] )
        print( colored( '*********************************************', 'white', attrs = [ 'bold' ] ).center( columns ) )


    def menu(self):
        print( colored( 'Welcome', 'white', attrs = [ 'bold' ] ).center( columns ) )
        print( colored( '1. Fetch All Customer', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
        print( colored( '2. Fetch Customer By Account No.', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
        print( colored( '3. Verify Customer', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
        print( colored( '4. Delete Customer', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
        print( colored( '5. Check Transaction of Customer', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
        print( colored( '6. Logout', 'yellow', attrs = [ 'bold' ] ).center( columns ) )
        choice = int( input( colored( 'Enter your choice(1-6): ', 'blue', attrs = [ 'bold' ] ) ) )
        return choice