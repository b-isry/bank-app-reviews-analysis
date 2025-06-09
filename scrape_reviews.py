from google_play_scraper import reviews_all
import pandas as pd

app = {
    "CBE": 'com.combanketh.mobilebanking',
    "BOA": 'com.boa.boaMobileBanking',  
    "Dashen": 'com.dashen.dashensuperapp'
}

all_reviews = []

for bank, app_id in app.items():
    print(f"fetching reviews for: {bank}")
    reviews = reviews_all(
        app_id,
        sleep_milliseconds=0,
        lang = 'en',
        country='et',
    )
    print(f"fetched {len(reviews)} reviews for {bank}")

    for r in reviews[:400]:
        all_reviews.append({
            'review':r['content'],
            'rating': r['score'],
            'date': r['at'].strftime('%Y-%m-%d'),
            'bank': bank,
            'source': 'Google Play'                  
        })

df = pd.DataFrame(all_reviews)
df.to_csv('./data/bank_reviews.csv', index=False)
print("Reviews saved to bank_reviews.csv")