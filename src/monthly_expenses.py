import pandas as pd
import re

def monthly_expenses():
    csv_path = "./csv_storage/202508.csv"

    exclude_keywords = [
        "まいばすけっと", "サミット", "サミット／ＮＦＣ", "CURSOR", "ＢＩＧＬＯＢＥ利用料",
        "ＵＱ　ｍｏｂｉｌｅご利用料金", "ファミリーマート", "セブン-イレブン",
        "ローソン", "NewDays", "ミニストップ"
    ]

    rows = []
    with open(csv_path, "r", encoding="cp932") as f:
        next(f)  # 1行目スキップ
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) < 3:
            continue

        date = parts[0]

        # 日付以降で最初に数値らしい要素が出るまでを「支払い名」として結合
        payname_parts = []
        amount = None
        for p in parts[1:]:
            p_stripped = p.strip()
            if re.match(r"^\d+$", p_stripped):  # 数値だけの列が来たら金額確定
                amount = int(p_stripped)
                break
            payname_parts.append(p_stripped)

        payname = " ".join(payname_parts)

        # 金額が見つからなかった場合はスキップ
        if amount is None:
            continue

        rows.append([payname, amount])

    df = pd.DataFrame(rows, columns=["支払い名", "金額"])

    # 除外ワード除去
    mask_exclude = df["支払い名"].apply(lambda x: any(k in str(x) for k in exclude_keywords))
    df_filtered = df[~mask_exclude]

    # 集計
    monthly_summary = df_filtered.groupby("支払い名", as_index=False)["金額"].sum()
    total_expense = monthly_summary["金額"].sum()

    print("📅 月ごとの支払い名別支出一覧（除外ワード含まず）")
    print(monthly_summary.sort_values("金額", ascending=False))
    print("\n💰 月合計支出:", total_expense, "円")

    monthly_summary.to_csv("monthly_expenses_filtered.csv", encoding="utf-8-sig", index=False)
