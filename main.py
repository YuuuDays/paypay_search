from src.combine import combine_count
from src.mitsui_monthly_expenses import monthly_expenses

# コンビニ

# combine_count()
csv_path = "./csv_storage/202509.csv"

#月支払い分類
result = monthly_expenses(csv_path)

# スプレットシート用のTSV(タブ区切り)で出力
for name, amount in result:
    print(f"{name},{amount:}")

