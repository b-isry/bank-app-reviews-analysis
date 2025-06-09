import pandas as pd

df = pd.read_csv('./data/bank_reviews.csv')
print(f"Initial reviews: {len(df)}")

df.drop_duplicates(subset=['review', 'rating', 'date', 'bank'], inplace=True)
print(f"After removing duplicates: {len(df)}")

df.dropna(subset=['review', 'rating', 'date', 'bank'], inplace=True)
print(f"After removing missing data: {len(df)}")

df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

df.dropna(subset=['date'], inplace=True)
print(f"After normalizing dates: {len(df)}")

df = df[['review', 'rating', 'date', 'bank', 'source']]  
df.to_csv('./data/bank_reviews_cleaned.csv', index=False)
print("Cleaned data saved to bank_reviews_cleaned.csv")
