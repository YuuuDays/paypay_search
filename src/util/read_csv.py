import pandas as pd

def read_csv(path: str, isMitsui: bool = True) -> pd.DataFrame:

    if isMitsui:
        encoding = "cp932"
    else: # paypay
        encoding = "utf-8"

    try:
        with open(path, "r", encoding= encoding) as f:
            next(f)  # 1行目スキップ
            lines = f.readlines()
            return lines
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None










