import unittest
from src.monthly_expenses import bai_num

# unittest.TestCase: 継承する親クラス（unittestの基本クラス）
"""
# 実際にはこういうことが起きている
test_instance = TestMonthlyExpenses()  # unittestが自動で作成
test_instance.test_normal_case()       # self = test_instance
"""
class TestMonthlyExpenses(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(bai_num(2), 4)

"""
その他assertメソッド
class TestMonthlyExpenses(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(bai_num(2), 4)      # 値が等しいか
    
    def test_zero_case(self):
        self.assertEqual(bai_num(0), 0)      # 0のテスト
    
    def test_negative_case(self):
        self.assertEqual(bai_num(-1), -2)    # 負の数のテスト
    
    def test_type_check(self):
        self.assertIsInstance(bai_num(5), int)  # 型チェック
    
    def test_true_case(self):
        self.assertTrue(bai_num(3) > 0)      # 条件が真か
"""

unittest.main()