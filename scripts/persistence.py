import pandas as pd
import oracledb
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Load cleaned CSV
csv_file_path = os.getenv("CSV_FILE_PATH", "./data/bank_reviews_cleaned.csv")
df = pd.read_csv(csv_file_path)

# Connect to Oracle XE
dsn = oracledb.makedsn(
    os.getenv("ORACLE_HOST", "localhost"),
    int(os.getenv("ORACLE_PORT", 1521)),
    service_name=os.getenv("ORACLE_SERVICE_NAME", "XEPDB1")
)

try:
    with oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=dsn
    ) as connection:
        with connection.cursor() as cursor:
            for index, row in df.iterrows():
                bank_name = row['bank']
                
                # Get bank_id
                cursor.execute(
                    "SELECT id FROM banks WHERE name = :bank_name",
                    bank_name=bank_name
                )
                result = cursor.fetchone()
                if not result:
                    print(f"Warning: Bank '{bank_name}' not found in banks table. Skipping row {index}.")
                    continue

                bank_id = result[0]

                # Insert review
                cursor.execute("""
                    INSERT INTO reviews (
                        review_text,
                        rating,
                        review_date,
                        bank_id,
                        source
                    ) VALUES (
                        :review_text,
                        :rating,
                        TO_DATE(:review_date, 'YYYY-MM-DD'),
                        :bank_id,
                        :source
                    )
                """,
                review_text=row['review'],
                rating=int(row['rating']),
                review_date=row['date'],
                bank_id=bank_id,
                source=row['source'])

            connection.commit()
    print("Data inserted successfully!")

except oracledb.Error as e:
    print("Error occurred while inserting data:", e)
