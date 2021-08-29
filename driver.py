# from BankingProj.Admin.adminMenu import AdminMenu
# from BankingProj.Admin.services.AdminService import AdminService
import config
import sys
# from Admin.adminMenu import hi
import Admin.adminMenu
import Customer.customerMenu
import sys
from termcolor import colored


if __name__ == "__main__":

    print( colored( 'hello', 'red' ), colored( 'world', 'magenta' ) )
    
    print( '***********************************************************' )
    print( 'Login as : ' )
    print( '1. Admin ' )
    print( '2. Customer ' )
    print( '3. Exit ' )
    login_type = int( input('1/2/3: ') )
    if login_type == 1:
        print( 'hii' )
        Admin.adminMenu.AdminMenu( )
        # Admin.adminMenu.AdminMenu.printMenu()
        # a.printMenu()
    elif login_type == 2:
        Customer.customerMenu.CustomerMenu( )



