# from BankingProj.Admin.adminMenu import AdminMenu
# from BankingProj.Admin.services.AdminService import AdminService
import shutil
from termcolor import colored
columns = shutil.get_terminal_size().columns
import config
import sys
# from Admin.adminMenu import hi
import Admin.adminMenu
import Customer.customerMenu
import sys



if __name__ == "__main__":

    print( colored( 'hello', 'red' ), colored( 'world', 'magenta' ) )
    print( colored( '***************************************************************************', 'red' ).center( columns ) )
    print( "{0:_>5}".format( colored( '-----LOGIN----- ', 'yellow' ).center( columns ) ) )
    print( "{0:_>2}".format( colored( '1. Admin ', 'magenta').center( columns ) ) )
    print( "{0:_>20}".format( colored( '2. Customer ', 'magenta').center( columns ) ) )
    print( "{0:_>20}".format( colored( '3. Exit ', 'magenta').center( columns ) ) )

    login_type = int( input( 'Enter 1/2/3: ' ) )
    
    if login_type == 1:
        Admin.adminMenu.AdminMenu( )

    elif login_type == 2:
        Customer.customerMenu.CustomerMenu( )



