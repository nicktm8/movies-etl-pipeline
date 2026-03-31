from extractor import extract
from transformer import transform
from loader import load

COUNTRIES = ["USA", "Russia", "UK", "South Korea"]

data = extract('data/movies.csv')

for country in COUNTRIES:
    df = transform(data, country)
    load(df, country)
    print(f"✅ {country} done!")
    