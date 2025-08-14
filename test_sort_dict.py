# 辞書の値を降順にソートする例

# サンプルデータ
payment_dict = {
    "ヒルトン": 15000,
    "ＡＭＡＺＯＮ": 5000,
    "マクドナルド": 1000,
    "タイムズカー": 20000,
    "ＪＲ東日本モバイルＳｕｉｃａ": 3000
}

print("元の辞書:")
print(payment_dict)
print()

# 方法1: sorted()でタプルのリストを作成
print("方法1: sorted()でタプルのリスト")
sorted_items = sorted(payment_dict.items(), key=lambda x: x[1], reverse=True)
for name, amount in sorted_items:
    print(f"{name}: {amount:,}円")
print()

# 方法2: 辞書内包表記で新しい辞書を作成
print("方法2: ソートされた辞書")
sorted_dict = dict(sorted(payment_dict.items(), key=lambda x: x[1], reverse=True))
for name, amount in sorted_dict.items():
    print(f"{name}: {amount:,}円")
print()

# 方法3: 上位3件のみ表示
print("方法3: 上位3件のみ表示")
top_3 = sorted(payment_dict.items(), key=lambda x: x[1], reverse=True)[:3]
for i, (name, amount) in enumerate(top_3, 1):
    print(f"{i}位: {name} - {amount:,}円")
print()

# 方法4: スプレッドシート貼り付け用（TSV形式）
print("方法4: スプレッドシート貼り付け用（TSV形式）")
print("支払名\t支払額")
for name, amount in sorted_items:
    print(f"{name}\t{amount:,}")
print()

# 方法5: スプレッドシート貼り付け用（CSV形式）
print("方法5: スプレッドシート貼り付け用（CSV形式）")
print("支払名,支払額")
for name, amount in sorted_items:
    print(f"{name},{amount:,}")
print()

# 方法6: 実際のデータでテスト（TSV形式）
print("方法6: 実際のデータでTSV形式出力")
actual_data = [('ＧＯＯＧＬＥ＊ＣＬＯＵＤ　ＸＷＸＣＶ６', 8), ('ｐｉｘｉｖＦＡＮＢＯＸ', 500), ('XAI LLC (PALO ALTO )', 747), ('しずおかマルシェ静岡ＳＡ上り', 1587), ('マクドナルド', 1770), ('中日本高速道路（株）東京支社', 1830), ('トウキユウパワ―サプライ', 2317), ('ＪＲ東海', 3450), ('東日本高速道路　関東 支社', 3870), ('Ｈ＆Ｍお台場', 4298), ('キュービックプラザ新横浜', 4415), ('ＪＲ東日本モバイルＳｕｉｃａ', 5000), ('はなの舞　三島南口店／ＮＦＣ', 6931), ('ＡＭＡＺＯＮ．ＣＯ．ＪＰ', 8608), ('目利きの銀次東京駅日本橋３丁目店', 12363), ('ヒルトントウキヨウオダイバ', 13050), ('ハイアツトセントリツク　ギンザ　トウ', 15180), ('タイムズカー', 28300)]

print("支払名\t支払額")
for name, amount in actual_data:
    print(f"{name}\t{amount:,}")
