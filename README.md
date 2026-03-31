# 🎬 Movies ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)
![openpyxl](https://img.shields.io/badge/openpyxl-3.0+-217346?style=flat&logo=microsoftexcel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)

An ETL pipeline that extracts movie data from a CSV file, calculates profitability per film, and exports the top 10 most profitable movies per country into formatted Excel files.

---

## ⚙️ Features

- Extracts movie data from a CSV source file
- Filters movies by country (supports multi-country entries e.g. `"UK, USA"`)
- Calculates profitability balance: `box_office - budget`
- Sorts films by balance in descending order
- Exports top 10 most profitable films per country to `.xlsx` files
- Applies number formatting in Excel (`1,000,000,000.00`)

---

## 🏗️ Project Structure

```
movies-etl-pipeline/
│
├── data/
│   └── movies.csv              # Input dataset
│
├── output/                     # Generated Excel files (auto-created)
│   ├── USA_top10.xlsx
│   ├── Russia_top10.xlsx
│   ├── UK_top10.xlsx
│   └── South_Korea_top10.xlsx
│
├── src/
│   ├── extractor.py            # CSV ingestion and type conversion
│   ├── transformer.py          # Filtering, balance calculation, sorting
│   ├── loader.py               # Excel export with openpyxl formatting
│   └── main.py                 # ETL pipeline entry point
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nicktm8/movies-etl-pipeline.git
cd movies-etl-pipeline
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the pipeline:
```bash
cd src
python main.py
```

---

## 📊 Output

For each country, an Excel file is generated in the `output/` folder with the following columns:

| Column | Description |
|---|---|
| `title` | Movie title |
| `release_year` | Year of release |
| `genre` | Movie genre(s) |
| `director` | Director name |
| `balance` | Profit: `box_office - budget` |

Example output — `USA_top10.xlsx`:

```
title                      release_year   genre                       director         balance
Avatar                     2009           Action, Adventure, Sci-Fi   James Cameron    2,610,246,000.00
Avengers: Endgame          2019           Action, Adventure, Sci-Fi   Anthony i Joe    2,442,000,000.00
Titanic                    1997           Drama, Romance              James Cameron    1,994,440,000.00
...
```

---

## 🧱 Architecture

The pipeline follows a strict **ETL (Extract → Transform → Load)** pattern with clear separation of concerns:

| Layer | File | Responsibility |
|---|---|---|
| Extract | `extractor.py` | Read CSV, convert numeric types |
| Transform | `transformer.py` | Filter by country, calculate balance, sort, select top 10 |
| Load | `loader.py` | Export to Excel, apply number formatting |
| Entry point | `main.py` | Orchestrate the full pipeline |

**Data flow:**
```
movies.csv → extractor.py → transformer.py → loader.py → country_top10.xlsx
```

---

## 🛠️ Planned Improvements

- [ ] Add `config.py` for centralized configuration (countries, paths, top N)
- [ ] Add logging instead of `print()` statements
- [ ] Add error handling for missing or malformed data
- [ ] Add unit tests for transformer logic
- [ ] Support additional output formats (JSON, PDF report)
- [ ] Visualize results with `matplotlib` or `seaborn`

---

## 🧠 Technical Highlights

- **ETL architecture** — strict separation between extraction, transformation, and loading
- **Robust filtering** — uses `str.contains()` to handle multi-country entries (e.g. `"UK, USA"`)
- **Type safety** — `pd.to_numeric(errors='coerce')` handles missing or malformed numeric values
- **Excel formatting** — `openpyxl` applies number formatting while preserving numeric data type for sorting
- **Reusable design** — `process_country()` accepts any country name, making it easy to extend

---

## Changelog

### v1.0.0 — Initial Release
- Add `extractor.py` for CSV ingestion and numeric type conversion
- Add `transformer.py` for country filtering and balance calculation
- Add `loader.py` for Excel export with openpyxl number formatting
- Add `main.py` as ETL pipeline entry point
- Support for USA, Russia, UK, and South Korea

---

## Contributing

Contributions, suggestions, and feedback are welcome.

1. Fork the repository
2. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```
3. Commit your changes:
```bash
git commit -m "feat: add your feature"
```
4. Push to your branch:
```bash
git push origin feature/your-feature-name
```
5. Open a Pull Request

If you spot a bug or have an idea, feel free to open an [issue](https://github.com/nicktm8/movies-etl-pipeline/issues).

---

## 👤 Author

Nick Tem  
GitHub: https://github.com/nicktm8