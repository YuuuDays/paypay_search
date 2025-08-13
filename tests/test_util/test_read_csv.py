import unittest
from unittest.mock import patch, mock_open
from src.util.read_csv import read_csv

class TestMonthlyExpenses(unittest.TestCase):
    csv_path = "./csv_storage/202508.csv"
    # 異常
    def test_read_csv_abnormal_case(self):
        self.assertEqual(read_csv(None),None)

    # 正常
    def test_read_csv_normal_case(self):
        # テスト用のCSVデータ（Shift-JISエンコーディングを想定）
        test_csv_data = """日付,支払い名,金額,カテゴリ,メモ,合計,備考
2025/07/04,目利きの銀次東京駅日本橋３丁目店,12363,１,１,12363,
2025/07/05,テスト店舗,1000,食費,テスト,1000,"""
        
        expected_line = "2025/07/05,テスト店舗,1000,食費,テスト,1000,"
        
        # ファイルオープンをモック
        with patch('builtins.open', mock_open(read_data=test_csv_data)):
            result = read_csv("dummy_path.csv")
            
            # 結果を検証
            self.assertIsNotNone(result)
            self.assertIn(expected_line, result)

"""
assertEqual(a, b)

assertNotEqual(a, b)
a != bであることを確かめる関数。

assertTrue(a)
a == Trueであることを確かめる関数。

assertFalse(a)
a == Falseであることを確かめる関数。

assertIn(a, b)
aがbに含まれるかどうかを調べる関数。
"""
unittest.main()