from extractor import extract
from transformer import transform
from loader import load
from config import INPUT_FILE, OUTPUT_DIR, COUNTRIES, TOP_NUMBER


data = extract(INPUT_FILE)

for country in COUNTRIES:
    df = transform(data, country, TOP_NUMBER)
    load(df, country, OUTPUT_DIR, TOP_NUMBER)
    print(f"✅ {country} done!")
