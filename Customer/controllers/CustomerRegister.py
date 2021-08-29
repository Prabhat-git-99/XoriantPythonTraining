import Customer.services.CustomerService
import datetime

import shutil
columns = shutil.get_terminal_size().columns

from termcolor import colored

class CustomerRegisteration( ):

    def __init__( self ) -> None:

        self.info = { }
        self.obj = Customer.services.CustomerService.CustomerService()

    
    def register( self, info, account_type ):
        self.info = info
        if account_type == 1:
            query = 'insert into customer ( accNo, name, address, phone, email, adhar, saving_acc ) values ( %s, %s, %s, %s, %s , %s, %s )'
        else:
            query = 'insert into customer ( accNo, name, address, phone, email, adhar, fixed_acc ) values ( %s, %s, %s, %s, %s , %s, %s )'

        self.obj.registerCustomer( self.info, query )