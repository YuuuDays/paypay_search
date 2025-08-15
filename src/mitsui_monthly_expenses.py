import pandas as pd
import re
from src.util.read_csv import read_csv

def monthly_expenses(csv_path: str, isMitsui: bool = True) -> list[tuple[str, int]]:
    

    exclude_keywords = [
        "まいばすけっと", "サミット", "サミット／ＮＦＣ", "CURSOR", "ＢＩＧＬＯＢＥ利用料",
        "ＵＱ　ｍｏｂｉｌｅご利用料金", "ファミリーマート", "セブン-イレブン",
        "ローソン", "NewDays", "ミニストップ","セブン－イレブン","ＣＵＲＳＯＲ，  ＡＩ  ＰＯＷＥＲＥＤ  Ｉ",
        "ＵＱ  ｍｏｂｉｌｅご利用料金","ＮｅｗＤａｙｓ","セブンーイレブン"
    ]

    # 三井住友とpaypayで分岐
    if isMitsui:
        isMitsui = True
    else:
        isMitsui = False

    # csvデータを読み込み&1行読み飛ばし値を返す
    lines = read_csv(csv_path,isMitsui)

    # null Check
    if not lines:
        print("恐らくcsvファイルが見つかりません")
        return None
    
    """
    空白行をスキップする
    """
    lines = skip_blank_lines(lines)

    """
    フィルターの実装(不要ワードが含まれている場合除去)
    """
    lines = filter_out_unwanted_words(lines, exclude_keywords)

    """
    支払い名と金額を取得 & 重複した支払い名と金額を合算する
    """
    payment_dict = get_payment_name_and_amount(lines)

    """
    金額が降順になるように並び替え
    """
    sorted_items = sorted(payment_dict.items(), key=lambda x: x[1], reverse=False)
    return sorted_items


        

# 空白飛ばし
def skip_blank_lines(lines: list[str]) -> list[str]:
    # [式 for 変数 in イテラブル if 条件]
    return [line for line in lines if line.strip()]
            #  ↑    ↑     ↑        ↑
            #  │    │     │        └─ 条件（空白でない場合のみ）
            #  │    │     └─ 元のリスト
            #  │    └─ 各要素を表す変数
            #  └─ 新しいリストに含める要素

# 不要ワード除去 
def filter_out_unwanted_words(lines: list[str], exclude_keywords: list[str]) -> list[str]:
    return [line for line in lines if not any(k in line for k in exclude_keywords)]

#支払い名と金額のみ (+ 最後の行は飛ばす) & 重複した支払い名と金額を合算する
def get_payment_name_and_amount(lines: list[str]) -> dict[str, int]:
    payment_dict = {}  # 辞書で管理
    
    for line in lines:
        parts = line.split(",")
        # print(parts)
     
        # 最後の不要な行を削除(合計金額を算出する行_のちに使うかもしれない)
        if parts[0] == "":
            break

        # 支払い名取得
        payment_name = parts[1].replace('"', "")
        
        # 金額取得（カンマ3個目以降から最初の数値を探す）
        amount = None
        for i in range(2, len(parts)):
            parts[i] = parts[i].replace('"', "")

            # 文字列か数値か判断
            if parts[i].strip().isdigit():
                
                amount = parts[i]
                break
        
        # 金額が見つからない場合の処理
        if amount is None:
            # print(f"警告: 金額が見つかりません (支払い名: {payment_name})")
            continue
        
        # 金額出ない場合、再度取得
        if not amount.isdigit():
            amount = parts[3]
        
        # 辞書に追加（重複時は自動で合算）
        try:
            amount_int = int(amount)
        except ValueError:
            print(f"警告: 数値に変換できません '{amount}' (支払い名: {payment_name})")
            continue
        
        payment_dict[payment_name] = payment_dict.get(payment_name, 0) + amount_int
    
    # print(payment_dict)

    return payment_dict




