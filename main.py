
from src.combine import combine_count
from src.mitsui_monthly_expenses import monthly_expenses
from src.util.csv_path_get_and_display import start


def main():

    #csvファイルパスの選択&取得&表示
    csv_path = start()
    
    # 月支払い分類
    result = monthly_expenses(csv_path)
    
    if result:
        print(f"\n=== 処理結果 ===")
        print("支払い名,支払額")
        for name, amount in result:
            print(f"{name},{amount}")
    else:
        print("処理に失敗しました")

if __name__ == "__main__":
    main()

