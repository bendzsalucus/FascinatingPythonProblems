from ProspectComplimentsAccount import ProspectComplimentsAccount


class Main:
    @staticmethod
    def run():
        print("Welcome to the Bank Account Simulator!")

        # Example setup for Prospect Compliments
        try:
            prospect_account = ProspectComplimentsAccount(50)
            print(f"Created {prospect_account.account_type()} with balance: {prospect_account.cur_bal}")
            
            prospect_account.money_deposit_check(100, src="cash")
            print(f"New balance after deposit: {prospect_account.cur_bal}")
            
            prospect_account.withdraw_amt(30)
            print(f"New balance after withdrawal: {prospect_account.cur_bal}")
            
            print(prospect_account.account_status())
        except ValueError as e:
            print(f"Error: {e}")

        print("Simulation complete!")


Main().run()