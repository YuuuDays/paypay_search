import os


def get_csv_files():
    """csv_storageディレクトリ内のCSVファイル一覧を取得"""
    csv_dir = "././csv_storage"
    csv_files = []
    
    if os.path.exists(csv_dir):
        for file in os.listdir(csv_dir):
            if file.endswith('.csv'):
                csv_files.append(file)
    
    return sorted(csv_files)

def display_csv_files(csv_files):
    """CSVファイル一覧を表示"""
    print("=== CSVファイル一覧 ===")
    if not csv_files:
        print("CSVファイルが見つかりません")
        return None
    
    for i, file in enumerate(csv_files, 1):
        print(f"{i}. {file}")
    
    print(f"{len(csv_files) + 1}. 終了")
    print()
    
    return csv_files  # ファイル一覧を返す

def get_user_selection(csv_files):
    """ユーザーの選択を取得"""
    while True:
        try:
            choice = input("処理したいCSVファイルの番号を入力してください: ")
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(csv_files):
                return csv_files[choice_num - 1]
            elif choice_num == len(csv_files) + 1:
                return None
            else:
                print(f"1から{len(csv_files) + 1}までの数字を入力してください")
        except ValueError:
            print("有効な数字を入力してください")
        except KeyboardInterrupt:
            print("\nプログラムを終了します")
            return None
        
def start():
    """メイン処理"""
    print("家計簿CSV処理プログラム")
    print("=" * 30)

        # CSVファイル一覧を取得
    csv_files = get_csv_files()
    
    # ファイル一覧を表示
    display_csv_files(csv_files)
    if not csv_files:
        return
    
    # ユーザーの選択を取得
    selected_file = get_user_selection(csv_files)
    if not selected_file:
        print("プログラムを終了します")
        return
    
    # 選択されたファイルを処理
    csv_path = f"./csv_storage/{selected_file}"
    print(f"\n選択されたファイル: {selected_file}")

    return csv_path