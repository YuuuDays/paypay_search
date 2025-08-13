from src.combine import combine_count
from src.monthly_expenses import monthly_expenses




# コンビニ
# combine_count()
csv_path = "./csv_storage/202508.csv"
#月支払い分類
result = monthly_expenses(csv_path)
print(result)