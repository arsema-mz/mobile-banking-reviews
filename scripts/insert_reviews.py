import cx_Oracle
import pandas as pd

# Oracle connection details
dsn = cx_Oracle.makedsn('localhost', 1521, service_name='XEPDB1')
username = 'bank_reviews_user'
password = 'Password'

# CSV file path
csv_file_path = '../data/combined_analysis_results.csv'

def insert_reviews():
    try:
        # Connect to Oracle
        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
        cursor = connection.cursor()
        print("Connected as:", connection.username)

        # Load CSV
        reviews_df = pd.read_csv(csv_file_path)
        print("Columns in DataFrame:", reviews_df.columns)

        insert_query = """
        INSERT INTO Reviews (review_id, bank_id, review_text, sentiment_score)
        VALUES (:1, NULL, :2, :3)
        """


        # Insert data row by row
        for _, row in reviews_df.iterrows():
            cursor.execute(insert_query, (
                int(row['review_id']),
                row['review'],
                float(row['sentiment_score'])
            ))

        connection.commit()
        print("✅ Data inserted successfully!")

    except cx_Oracle.DatabaseError as e:
        print(f"❌ Error inserting data: {e}")

    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    insert_reviews()
