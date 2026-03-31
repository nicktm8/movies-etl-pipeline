import pandas as pd

def extract(file_path):
    data = pd.read_csv(file_path)
    data['box_office'] = pd.to_numeric(data['box_office'], errors='coerce')
    return data 
