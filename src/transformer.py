from config import TOP_NUMBER

def transform(data, country_name, TOP_NUMBER):
    country = data[data["country"].str.contains(country_name, na=False)].copy()
    country['balance'] = country['box_office'] - country['budget']
    country_sorted = country.sort_values(by='balance', ascending=False).head(TOP_NUMBER)
    return country_sorted[["title", "release_year", "genre", "director", "balance"]].copy()
