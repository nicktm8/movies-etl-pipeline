from config import TOP_NUMBER

def transform(data, country_name, TOP_NUMBER):
    try:
        country = data[data["country"].str.contains(country_name, na=False)].copy()

        if country.empty:
            print(f"⚠️ No films found for: {country_name}")
            return None
        
        country['balance'] = country['box_office'] - country['budget']
        country_sorted = country.sort_values(by='balance', ascending=False).head(TOP_NUMBER)
        
        return country_sorted[["title", "release_year", "genre", "director", "balance"]].copy()
    
    except Exception as e:
        print(f"❌ Error transforming data for {country_name}: {e}")
        raise
