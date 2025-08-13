import unittest
from src.util.read_csv import read_csv

class TestMonthlyExpenses(unittest.TestCase):
    csv_path = "./csv_storage/202508.csv"
    def test_read_csv_abnormal_case(self):
        self.assertEqual(read_csv(None),None)

unittest.main()