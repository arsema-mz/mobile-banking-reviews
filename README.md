# Mobile Banking Reviews Analysis

## Methodology

1. **Data Collection**: Reviews were scraped from the Google Play Store using the `google-play-scraper` library for three Ethiopian banks (CBE, BOA, Dashen).
2. **Data Cleaning**: Preprocessing was done to remove duplicates and normalize dates, ensuring a clean dataset.
3. **Output**: A total of 1,200 reviews were collected and cleaned, saved as `cleaned_reviews.csv`.

## Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/mobile-banking-reviews.git
cd mobile-banking-reviews
pip install -r requirements.txt 
