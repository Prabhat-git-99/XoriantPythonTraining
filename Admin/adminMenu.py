# from BankingProj.Admin.services.AdminService import AdminService
from typing import Container
from mysql import connector
import Admin.services.AdminService
import Admin.controller.AdminController

class AdminMenu():

    def __init__(self) -> None:
        self.name = ''
        self.password = ''
        self.printMenu()


    def showFeedBack( self, msg ):
        print(msg)

    def printMenu( self ):

        print('ADMIN PANEL')
        flag = True
        self.name = input('Enter Name: ')
        self.password = input('Enter Password: ')
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
                print('Please enter correct credentials!')
                flag = False
                break

    def checkTransaction(self):
        # self.fetchAllCustomer( )
        acc_no = input( 'Enter Account Number: ' )
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.checkTransaction( acc_no )
        print( records )

    def deleteCustomer(self):
        print('Which customer you want to ')
        self.fetchAllCustomer( )
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.deleteCustomer( )

    def verifyCustomer(self):
        print('Which customer you want to ')
        self.fetchAllCustomer( )
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.verifyCustomer( )


    def fetchById(self):
        id = int(input('Enter Account No. :'))
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.fetchSingleCustomer( id )
        self.printRecord( records )
    
    def fetchAllCustomer(self):
        print('All Customers')
        obj = Admin.controller.AdminController.AdminController( self.name, self.password )
        records = obj.fetchAllCustomer(  )
        for row in records:
            self.printRecord( row )
                    
    def printRecord( self, row ):
        print('*********************************************')
        print('CustomerId : ', row[0])
        print('AccNo : ', row[1])
        print('Name : ', row[2])
        print('Address : ', row[3])
        print('Mobile : ', row[4])
        print('email : ', row[5])
        print('Aadhar : ', row[6])
        print('Status( 1-Verified, 0-Not Verified ) : ', row[7])
        print('*********************************************')


    def menu(self):
        print( 'Welcome' )
        print( '1. Fetch All Customer' )
        print( '2. Fetch Customer by AccNo' )
        print( '3. Verify Customer' )
        print( '4. Delete Customer' )
        print( '5. Check Transactions of Customer' )
        print( '6. Logout' )
        choice = int(input('Enter your choice(1-6): ' ) )
        return choice