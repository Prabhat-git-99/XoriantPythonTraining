import Customer.services.CustomerService
import datetime

class CustomerController( ):

    def __init__(self, accNo, password ) -> None:
        self.accNo = accNo
        self.password = password
        self.saving_bal = ''
        self.fixed_bal = ''
        self.obj = Customer.services.CustomerService.CustomerService()
    
    def customerLogin( self ):

        found = self.obj.customerLogin( self.accNo, self.password )
        if ( found[ 'user' ] and found[ 'user' ][ 6 ] ):

            password = found[ 'account' ][ 3 ]
            if ( password == self.password ):
                return { 'user': found[ 'user' ], 'account': found[ 'account' ], 'status': 'found' }
            else:
                return { 'user': { }, 'account': { }, 'status': 'not found' }

        else:
            return { 'user': { }, 'status': "not found or your account is not approved" }
    
    def withdraw( self, account_type, status ):
        
        if status != 'approved':
            print( 'You account is not approved yet!' )
            return

        amount = input( 'Enter amount to withdraw: ' )
        bal = self.fetchBalance( self.accNo, account_type )
        print( bal )
        print( account_type )
        if account_type == 'saving':
            bal = bal[ 1 ]
            print( bal )
            if int( bal ) < int( amount ):
                print( 'Insufficient Balance!' )
            else:
                new_bal = int(bal) - int(amount)
                query = 'UPDATE account set balance_saving=%s WHERE acc_no=%s'
                found = self.obj.withdraw( query, self.accNo, str( new_bal ) )
                query = 'insert into transaction ( accNo, to_acc_no, amount_transfered, date, trans_type, before_bal, updated_bal ) values ( %s, %s, %s , %s, %s, %s, %s )'
                found = self.obj.updateTransaction( query, self.accNo, "self", amount, datetime.datetime.now( ), "withdraw", bal, new_bal  )

        else:
            bal = bal[ 2 ]
            print( bal )
            if int( bal ) < int( amount ):
                print( 'Insufficient Balance!' )
            else:
                new_bal = int(bal) - int(amount)
                query = 'UPDATE account set balance_fixed=%s WHERE acc_no=%s'
                found = self.obj.withdraw( query, self.accNo, str( new_bal ) )
                query = 'insert into transaction ( accNo, to_acc_no, amount_transfered, date, trans_type, before_bal, updated_bal ) values ( %s, %s, %s , %s, %s, %s, %s )'
                found = self.obj.updateTransaction( query, self.accNo, "self_fixed", amount, datetime.datetime.now( ), "withdraw_fixed", bal, new_bal  )



    def deposit( self, account_type, status ):

        if status != 'approved':
            print( 'You account is not approved yet!' )
            return

        amount = input( 'Enter amount to deposit: ' )
        bal = self.fetchBalance( self.accNo, account_type )
        # print( bal )
        print( account_type )
        if account_type == 'saving':
    
            new_bal = int(bal[ 1 ]) + int( amount )
            print( bal[ 1 ], amount, new_bal )
            query = 'UPDATE account set balance_saving=%s WHERE acc_no=%s'
            found = self.obj.withdraw( query, self.accNo, str( new_bal ) )
            # if ( found ):
            print('inside found*****')
            query = 'insert into transaction ( accNo, to_acc_no, amount_transfered, date, trans_type, before_bal, updated_bal ) values ( %s, %s, %s , %s, %s, %s, %s )'
            found = self.obj.updateTransaction( query, self.accNo, "self", amount, datetime.datetime.now(), "deposit", bal[ 1 ], new_bal  )

        else:
            new_bal = int( bal[ 2 ] ) + int( amount )
            print( bal[ 1 ], amount, new_bal )
            query = 'UPDATE account set balance_fixed=%s WHERE acc_no=%s'
            found = self.obj.withdraw( query, self.accNo, str( new_bal ) )
            query = 'insert into transaction ( accNo, to_acc_no, amount_transfered, date, trans_type, before_bal, updated_bal ) values ( %s, %s, %s , %s, %s, %s, %s )'
            found = self.obj.updateTransaction( query, self.accNo, "self_fixed", amount, datetime.datetime.now(), "deposit_fixed", bal[ 1 ], new_bal  )

    def fetchBalance( self, accNo, account_type ):

        query = 'SELECT * FROM account WHERE acc_no=%s'
        bal = self.obj.fetchBalance( query, accNo )        
        return bal


    def transferMoney( self, to_acc ):

        query = 'SELECT * FROM account WHERE acc_no=%s'
        bal_from = self.obj.fetchBalance( query, self.accNo )
        bal_to = self.obj.fetchBalance( query, to_acc )

        balance_from = bal_from[ 1 ]
        amt = int( input( 'Enter amount to be Transfered: ' ) )
        real_amt = amt

        if amt > int( balance_from ):
            print( 'Insufficient Balance!' )
            return
        
        query = 'UPDATE account set balance_saving=%s WHERE acc_no=%s'
        amt = int( balance_from ) - amt 
        found = self.obj.withdraw( query, self.accNo, str( amt ) )

        query = 'UPDATE account set balance_saving=%s WHERE acc_no=%s'
        amt = int( bal_to[ 1 ] ) + real_amt
        found = self.obj.withdraw( query, to_acc, str( amt ) )




