import pandas as pd

# === 設定 ===
csv_path = "transactions.csv"  # CSVファイルのパス
target_word = "サミットストア"  # 抽出したい単語
date_column = "取引日"         # 日付が入っている列名
amount_column = "出金金額（円）"  # 金額が入っている列名

# === CSV読み込み ===
df = pd.read_csv("./csv_storage/Transactions_20240811-20250811.csv")

# 金額を数値化（カンマ除去、欠損は0）
df[amount_column] = (
    df[amount_column]
    .astype(str)
    .str.replace(",", "")
    .replace("-", "0")
    .astype(int)
)

# 日付をdatetime型に変換
df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

# 特定の単語を含む行を抽出
target_df = df[df[df.columns].apply(lambda row: row.astype(str).str.contains(target_word, case=False).any(), axis=1)]

# 月ごとの合計 → 平均
monthly_avg = target_df.groupby(target_df[date_column].dt.to_period("M"))[amount_column].sum().mean()

print(f"『{target_word}』を含む取引の月平均: {monthly_avg:.0f}円")
