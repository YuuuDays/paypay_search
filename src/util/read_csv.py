import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    try:
        with open(path, "r", encoding="cp932") as f:
            next(f)  # 1行目スキップ
            lines = f.readlines()
            return lines
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None










