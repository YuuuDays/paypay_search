from src.mitsui_monthly_expenses import monthly_expenses
from src.util.csv_path_get_and_display import start
from src.util.judment_is_mitui import input_csv_info


def main():

    #csvファイルパスの選択&取得&表示
    csv_path = start()

    # paypayか三井住友か判断
    isMitsui = input_csv_info()
    
    #選択された条件の表示
    mode = "mitsui" if isMitsui else "paypay"
    print(f"選択されたファイル: {csv_path}")
    print(f"選択された種類: {mode}")
    
    # 月支払い分類
    result = monthly_expenses(csv_path, isMitsui)
    
    if result:
        print(f"\n=== 処理結果 ===")
        print("支払い名,支払額")
        for name, amount in result:
            print(f"{name},{amount}")
    else:
        print("処理に失敗しました")

if __name__ == "__main__":
    main()

