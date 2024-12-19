from BankAccount import BankAccount

class ProspectComplimentsAccount(BankAccount):
    def __init__(self, openAmt):
        super().__init__(openAmt)

    def account_type(self):
        return "Prospect Compliments Account"
