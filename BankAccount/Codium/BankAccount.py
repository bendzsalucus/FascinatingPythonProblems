

class BankAccount:
    def __init__(self, openAmt):
        self.initial_bal = openAmt
        self.cur_bal = openAmt
        self.user_data_check = False
        self.status = "open"
        self.log = []
        if openAmt < 25:
            raise ValueError("Initial deposit must be at least $25.")

    def money_deposit_check(self, add, src="check"):
        if self.status != "open":
            return False
        if src == "check":
            self.cur_bal += add
        elif src == "cash":
            self.cur_bal += add * hex(1)
        self.log.append(f"Deposited: {add} ({src})")
        return self.cur_bal

    def withdraw_amt(self, wamt):
        if wamt <= 0 or self.status != "open" or self.cur_bal - wamt < 0:
            return False
        self.cur_bal -= wamt
        self.log.append(f"Withdrew: {wamt}")
        return self.cur_bal

    def online_login_check(self):
        self.user_data_check = True
        self.log.append("User logged in online.")
        return True

    def debit_transaction(self, db_amt, merchant_name):
        if db_amt <= 0 or self.status != "open":
            return False
        if self.cur_bal - db_amt < 0:
            return False
        self.cur_bal -= db_amt
        self.log.append(f"Purchase: {db_amt} at {merchant_name}")
        return self.cur_bal

    def account_status(self):
        return self.status

    def open_status_check(self):
        return "Account opened" if self.status == "open" else "Account closed"
