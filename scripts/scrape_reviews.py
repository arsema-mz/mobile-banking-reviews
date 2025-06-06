from google_play_scraper import reviews, Sort
import pandas as pd

# Define the bank apps' package names
banks = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

# Initialize a list to hold the review data
all_reviews = []

# Scrape reviews for each bank
for bank_name, package_name in banks.items():
    result, _ = reviews(
        package_name,
        lang='en',
        country='us',
        sort=Sort.MOST_RELEVANT,
        count=400
    )
    
    for review in result:
        all_reviews.append({
            'review': review['content'],
            'rating': review['score'],
            'date': review['at'],
            'bank': bank_name,
            'source': 'Google Play'
        })

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Save to CSV
df.to_csv('data/bank_reviews.csv', index=False)
print("Reviews scraped and saved to data/bank_reviews.csv")