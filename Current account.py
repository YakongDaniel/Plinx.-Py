  #Current account with no restrictions

class CurrentAccount(Account):
    def __init__(self, account_number, your_name, balance=0.0):
        super().__init__(account_number, your_name, balance)
