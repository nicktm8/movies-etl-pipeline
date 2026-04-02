import pandas as pd

def extract(file_path):
    try:
        data = pd.read_csv(file_path)
        data['box_office'] = pd.to_numeric(data['box_office'], errors='coerce')
        return data
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        raise
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        raise
     