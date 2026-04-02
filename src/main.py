from extractor import extract
from transformer import transform
from loader import load
from config import INPUT_FILE, OUTPUT_DIR, COUNTRIES, TOP_NUMBER

try:
    data = extract(INPUT_FILE)
except Exception:
    print("❌ Pipeline stopped — could not read input file.")
    exit(1)
    
for country in COUNTRIES:
    try:
        df = transform(data, country, TOP_NUMBER)
        if df is not None:
            load(df, country, OUTPUT_DIR, TOP_NUMBER)
            print(f"✅ {country} done!")
            print("--------")
    except Exception:
        print(f"⚠️ Skipping {country} — continuing with next.")
        continue
