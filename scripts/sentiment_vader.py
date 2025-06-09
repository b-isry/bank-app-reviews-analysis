import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv('./data/bank_reviews_cleaned.csv')

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'
df['commpound_score'] = df['review'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
df['sentiment_label'] = df['commpound_score'].apply(get_sentiment)

sentiment_summary = df.groupby(['bank', 'rating', 'sentiment_label']).size().reset_index(name='count')
sentiment_summary.to_csv('./data/sentiment_summary.csv', index=False)

df.to_csv('./data/bank_reviews_with_sentiment.csv', index=False)
print("Sentiment analysis completed and saved to bank_reviews_with_sentiment.csv")