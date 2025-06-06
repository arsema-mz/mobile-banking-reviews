import pandas as pd

def preprocess_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing data
    df = df.dropna()
    
    # Normalize dates
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    
    # Save processed data
    df.to_csv('data/processed_bank_reviews.csv', index=False)

if __name__ == "__main__":
    preprocess_data('data/bank_reviews.csv')