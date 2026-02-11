# K4K_TowContact_Scraper

K4K Python scraper to collect tow company contacts across US and CA.

## Features

- Scrapes automotive yard listings from ScrapMonster
- **Automatic pagination support** - loops through all pages to collect all scrapyards
- **Duplicate removal** - automatically removes duplicate entries based on company name and address
- Extracts Company, Location, YardBrief, and Address information
- Error handling for missing fields
- Exports data to Excel (.xlsx) format with formatted headers

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ALK4K/K4K_TowContact_Scraper.git
cd K4K_TowContact_Scraper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the scraper:
```bash
python scraper.py
```

This will scrape automotive yard listings from:
`https://www.scrapmonster.com/scrap-yard/material/automotive/746`

**The scraper will automatically loop through all pages** and collect all available scrapyard listings. Duplicates are automatically removed based on company name and address.

The output will be saved to `automotive_yards.xlsx` in the current directory.

## Output Format

The Excel file contains the following columns:
- **Company**: Company name
- **Location**: Location/city
- **YardBrief**: Brief description of the yard
- **Address**: Full address

## Requirements

- Python 3.6+
- requests
- beautifulsoup4
- openpyxl
- lxml

See `requirements.txt` for specific versions.
