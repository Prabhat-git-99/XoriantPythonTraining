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
            query = 'insert into customer ( accNo, name, address, phone, email, adhar, saving_acc, opening_saving_date ) values ( %s, %s, %s, %s, %s , %s, %s, %s )'
        else:
            query = 'insert into customer ( accNo, name, address, phone, email, adhar, fixed_acc, opening_fixed_date ) values ( %s, %s, %s, %s, %s , %s, %s, %s )'

        self.obj.registerCustomer( self.info, query )

    def openSavingFixedAccount( self, account_number, account_type ):
        if account_type == 1:
            query = "UPDATE customer set saving_acc='requested', opening_saving_date=%s WHERE accNo=%s"
            found = self.obj.openSavingFixedAccount( query, account_number, datetime.datetime.now( ) )
        else:
            query = "UPDATE customer set fixed_acc='requested', opening_fixed_date=%s WHERE accNo=%s"
            found = self.obj.openSavingFixedAccount( query, account_number, datetime.datetime.now( ) )

        