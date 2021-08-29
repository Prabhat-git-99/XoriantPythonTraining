class User():

    def __init__(self, name, address, phone, email, adhar ) -> None:
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.adhar = adhar
    
    def display_user( self ):

        print( 'User Detail')
        print( 'Name: ', self.name )
        print( 'Address: ', self.address )
        print( 'Phone: ', self.phone )
        print( 'Email: ', self.email )
        print( 'Aadhar: ', self.adhar )

# accNo varchar(45) PK 
# acc_type