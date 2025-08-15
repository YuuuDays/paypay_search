
def input_csv_info():
    """ユーザーの選択を取得"""
    while True:
        try:
            print("1.三井住友銀行")
            print("2.paypay")
            choice = input("どっちの種類のcsvを使う?: ")
            choice_num = int(choice)
            
            if choice_num == 1:
                return True
            elif choice_num == 2:
                return False
            else:
                print(f"1か2の数字を入力してください")
        except ValueError:
            print("有効な数字を入力してください")
        except KeyboardInterrupt:
            print("\nプログラムを終了します")
            return None


