import pandas as pd

# === 設定 ===
csv_path = "transactions.csv"  # CSVファイルのパス
date_column = "取引日"         # 日付列
amount_column = "出金金額（円）"  # 金額列

# コンビニ系キーワード
conbini_keywords = ["ファミリーマート", "セブン-イレブン", "ローソン", "NewDays", "ミニストップ"]

# === CSV読み込み ===
df = pd.read_csv("./csv_storage/Transactions_20240811-20250811.csv")

# 金額を数値化
df[amount_column] = (
    df[amount_column]
    .astype(str)
    .str.replace(",", "")
    .replace("-", "0")
    .astype(int)
)

# 日付をdatetime型に変換
df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

# コンビニ系の取引を抽出
conbini_df = df[df["取引先"].apply(lambda x: any(k in str(x) for k in conbini_keywords))]

# 月ごとの支払い合計
monthly_totals = conbini_df.groupby(conbini_df[date_column].dt.to_period("M"))[amount_column].sum()

# 1年分の平均（全月合計 ÷ 月数）
yearly_avg = monthly_totals.mean()

# === 結果表示 ===
print("📅 月ごとのコンビニ支払い額")
print(monthly_totals)

print(f"\n📊 1年間のコンビニ平均支払い額（1か月あたり）: {yearly_avg:.0f}円")
