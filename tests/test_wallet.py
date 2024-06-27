import unittest
from src.wallet import Wallet
from src.record import Record


class TestWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet('test_records.txt')
        self.wallet.records = [
            Record('2024-05-02', 'Expense', 1500, 'Grocery shopping'),
            Record('2024-05-03', 'Income', 30000, 'Salary')
        ]
        self.wallet.save_records()

    def tearDown(self):
        import os
        os.remove('test_records.txt')

    def test_get_balance(self):
        income, expenses, balance = self.wallet.get_balance()
        self.assertEqual(income, 30000)
        self.assertEqual(expenses, 1500)
        self.assertEqual(balance, 28500)

    def test_add_record(self):
        record = Record('2024-06-01', 'Income', 5000, 'Bonus')
        self.wallet.add_record(record)
        self.assertEqual(len(self.wallet.records), 3)

    def test_edit_record(self):
        new_record = Record('2024-05-02', 'Expense', 1600, 'New groceries')
        self.wallet.edit_record(0, new_record)
        self.assertEqual(self.wallet.records[0].amount, 1600)

    def test_search_records(self):
        results = self.wallet.search_records(category='Income')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, 'Salary')


if __name__ == '__main__':
    unittest.main()
