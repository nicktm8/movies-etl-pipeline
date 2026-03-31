def transform(data, country_name):
    country = data[data["country"].str.contains(country_name, na=False)].copy()
    country['balance'] = country['box_office'] - country['budget']
    country_sorted = country.sort_values(by='balance', ascending=False).head(10)
    return country_sorted[["title", "release_year", "genre", "director", "balance"]].copy()
