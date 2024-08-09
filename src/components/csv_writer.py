import pandas as pd

def write_to_csv(data: pd.DataFrame, file_path: str):
    data.to_csv(file_path, index=False)