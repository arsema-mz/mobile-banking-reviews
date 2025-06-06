# Mobile Banking Reviews Analysis

# Overview

This project aims to collect and analyze customer reviews for three mobile banking applications available on the Google Play Store. By leveraging web scraping techniques, we gather insights into user experiences, ratings, and trends over time. The analysis of these reviews can help identify strengths and weaknesses in the banking apps, providing valuable feedback for developers and stakeholders.
# Methodology

## Web Scraping

1. **Objective**: The goal was to collect reviews, ratings, dates, and app names for three mobile banking applications.
  
2. **Data Source**: Used the `google-play-scraper` library to extract data from the Google Play Store.

3. **Targeted Apps**: 
    - Commercial Bank of Ethiopia (CBE)
    - Bank of Africa (BOA)
    - Dashen Bank

4. **Data Collection**:
    - Scraped **400+ reviews** for each bank, targeting a total of approximately **1,200 reviews**.
    - Collected the following data points:
        - Review content
        - Rating (1-5)
        - Date of the review
        - Bank name
        - Source (Google Play Store)

## Data Preprocessing

1. **Loading Data**: The raw review data was loaded from a CSV file.

2. **Cleaning Steps**:
    - **Removing Duplicates**: Ensured that each review was unique.
    - **Handling Missing Data**: Dropped any rows with missing values to maintain data integrity.
    - **Normalizing Dates**: Converted date formats to a standard YYYY-MM-DD format for consistency.

3. **Saving Processed Data**: The cleaned data was saved to a new CSV file for further analysis.

## Tools and Libraries

- Python
- pandas
- google-play-scraper
## Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/mobile-banking-reviews.git
cd mobile-banking-reviews
pip install -r requirements.txt 
