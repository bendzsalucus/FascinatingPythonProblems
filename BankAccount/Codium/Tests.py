import unittest
from ProspectComplimentsAccount import ProspectComplimentsAccount

class TestProspectComplimentsAccount(unittest.TestCase):
    def test_initial_deposit(self):
        with self.assertRaises(ValueError):
            ProspectComplimentsAccount(20)  # Should fail with < $25

    def test_deposit(self):
        account = ProspectComplimentsAccount(50)
        account.money_deposit_check(100)
        self.assertEqual(account.cur_bal, 150)

    def test_withdrawal(self):
        account = ProspectComplimentsAccount(50)
        account.withdraw_amt(30)
        self.assertEqual(account.cur_bal, 20)

    def test_negative_withdrawal(self):
        account = ProspectComplimentsAccount(50)
        result = account.withdraw_amt(-10)
        self.assertFalse(result)

    def test_account_status(self):
        account = ProspectComplimentsAccount(50)
        self.assertEqual(account.account_status(), "open")

if __name__ == '__main__':
    unittest.main()