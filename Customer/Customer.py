class Customer( ):

    def __init__(self, name, accNo, address, phone, email, adhar, status, saving_acc, fixed_acc ) -> None:
        
        self.name = name
        self.accNo = accNo
        self.address = address
        self.phone = phone
        self.email = email
        self.adhar = adhar
        self.status = status
        self.saving_acc = saving_acc
        self.fixed_acc = fixed_acc
        print( 'Inititated.. ')
    
    def getDetails( self ):

        return {
            'name': self.name,
            'accNo': self.accNo,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'adhar': self.adhar,
            'status': self.status,
            'saving_acc': self.saving_acc,
            'fixed_acc': self.fixed_acc
        }

    def set_name( self, name ):
        # print('seting name')
        self.name = name
    
    def set_acc( self, accNo ):
        self.accNo = accNo

    def set_address( self, address ):
        self.address = address

    def set_phone( self, phone ):
        self.phone = phone
    
    def set_email( self, email ):
        self.email = email
    
    def set_adhar( self, adhar ):
        self.adhar = adhar
    
    def set_status( self, status ):
        self.status = status
    
    def set_saving( self, saving_acc ):
        self.saving_acc = saving_acc
    
    def set_fixed( self, fixed_acc ):
        self.fixed_acc = fixed_acc
