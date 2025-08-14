import unittest
from src.mitsui_monthly_expenses import *
from unittest.mock import patch

# unittest.TestCase: 継承する親クラス（unittestの基本クラス）
"""
# 実際にはこういうことが起きている
test_instance = TestMonthlyExpenses()  # unittestが自動で作成
test_instance.test_normal_case()       # self = test_instance
"""
class TestMonthlyExpenses(unittest.TestCase):
    """
    基本的な応答
    """
    # def test_1_basic_csv_reading(self):
    #     test_csv_data = [
    #     "2025/07/01,テスト店舗,1000,食費,テスト,1000,\n",
    #     "2025/07/02,テスト店舗2,2000,食費,テスト2,2000,\n"]
        
    #     # モックでread_csvを置き換えて、そのまま返すだけ
    #     with patch('src.monthly_expenses.read_csv', return_value=test_csv_data):
    #         result = monthly_expenses("./dummy.csv")
    #         self.assertEqual(result, test_csv_data)  # ← 何もテストしていない
    # 空のファイル
    def test_2(self):
        with patch('src.monthly_expenses.read_csv', return_value=None):
            result = monthly_expenses("./empty.csv")
            self.assertEqual(result, None)

    """
    空白行をスキップする
    """
    def test_3_skip_blank_lines(self):
        test_csv_data = [
        "2025/07/01,テスト店舗,1000,食費,テスト,1000,\n",

        "2025/07/02,テスト店舗2,2000,食費,テスト2,2000,\n",]
        
        expected_csv_data = [
        "2025/07/01,テスト店舗,1000,食費,テスト,1000,\n",
        "2025/07/02,テスト店舗2,2000,食費,テスト2,2000,\n",]
        
        result = skip_blank_lines(test_csv_data)
        self.assertEqual(result, expected_csv_data)

    """
    フィルターの実装(不要ワードが含まれている場合除去)
    """
    def test_4_filter_out_unwanted_words(self):
        test_csv_data = [
        "2025/07/01,テスト店舗,1000,食費,テスト,1000,\n",
        "2025/07/03,CURSOR,1000,食費,テスト,1000,\n",
        "2025/07/02,テスト店舗2,2000,食費,テスト2,2000,\n",]
        
        expected_csv_data = [
        "2025/07/01,テスト店舗,1000,食費,テスト,1000,\n",
        "2025/07/02,テスト店舗2,2000,食費,テスト2,2000,\n",]
    
        exclude_keywords = ["CURSOR"]
        result = filter_out_unwanted_words(test_csv_data, exclude_keywords)
        self.assertEqual(result, expected_csv_data)


        
    """
    支払い名と金額を取得 & 重複した支払い名と金額を合算する
    """
    def test_5_get_payment_name_and_amount(self):
        test_csv_data = [
        "2025/07/01,テスト店舗,1000,食費,テスト,1000,\n",
        "2025/07/02,テスト店舗2,2000,食費,テスト2,2000,\n",
        "2025/07/02,テスト店舗2,2000,食費,テスト2,2000,\n",]
        
        expected_csv_data = {"テスト店舗":1000,"テスト店舗2":4000}

        result = get_payment_name_and_amount(test_csv_data)
        self.assertEqual(result, expected_csv_data)

    
    # 別のcsvファイルでテスト
    def test_6_get_payment_name_and_amount_2(self):
        test_csv_data = [
        "2025/8/9,ＪＲ東海,ご本人,1回払い,,'25/09,4380,4380,,,,,\n",
        "2025/07/02,テスト店舗2,2000,食費,テスト2,2000,\n",
        "2025/07/02,テスト店舗2,2000,食費,テスト2,2000,\n",]
        expected_csv_data = {"ＪＲ東海":4380,"テスト店舗2":4000}

        result = get_payment_name_and_amount(test_csv_data)
        self.assertEqual(result, expected_csv_data)
        
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