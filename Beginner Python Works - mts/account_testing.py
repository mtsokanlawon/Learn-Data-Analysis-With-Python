
class account:
    
    def __init__(self, account_number, account_name, opening_deposit, account_type
    ):
        self.account_number = account_number
        self.account_name = account_name
        self.opening_deposit = opening_deposit
        self.account_type = account_type

    def deposit(self, deposited_amount):
        self.opening_deposit + deposited_amount
        print( "deposited amount:" + str(deposited_amount))
        return deposited_amount

    def withdraw(self, withdrawn_amount):
        self.opening_deposit - withdrawn_amount
        print("withdrawn amount:" + str(withdrawn_mount))
        return withdrawn_amount

    
    def __str__(self):
        return "account number:" + self.account_number + "\n" + "name: " + self.account_name + "\n" + "Opening deposit:" + str(self.opening_deposit) + "\n" + "Account type: " + self.account_type + "\n" + "-"*25
        
        
class get_balance(account):
        def __init__()
        