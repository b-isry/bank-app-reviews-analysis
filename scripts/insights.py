import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv("./data/bank_reviews_with_sentiment.csv")

print(df.head())


# Separate positive and negative reviews
positive_reviews = df[df['sentiment_label'] == 'positive']
negative_reviews = df[df['sentiment_label'] == 'negative']

# Tokenize (simplistic example)
positive_words = ' '.join(positive_reviews['review']).lower().split()
negative_words = ' '.join(negative_reviews['review']).lower().split()

# Get top 10 words (excluding stopwords)
stopwords = set(['the', 'is', 'and', 'to', 'it', 'a', 'of', 'for', 'on', 'in', 'this', 'that', 'with'])
pos_counts = Counter(w for w in positive_words if w not in stopwords)
neg_counts = Counter(w for w in negative_words if w not in stopwords)

print("Top 10 positive keywords:")
print(pos_counts.most_common(10))

print("\nTop 10 negative keywords:")
print(neg_counts.most_common(10))

# Compare banks by sentiment score and average rating
bank_summary = df.groupby('bank').agg({
    'commpound_score': 'mean',
    'rating': 'mean'
}).reset_index()

print("Bank Summary:")
print(bank_summary)

# Visualize sentiment score and rating per bank
sns.barplot(x='bank', y='commpound_score', data=bank_summary)
plt.title('Average Sentiment Score per Bank')
plt.ylabel('Sentiment Score')
plt.xlabel('Bank')
plt.savefig('./plots/commpound_score_per_bank.png')
plt.show()

sns.barplot(x='bank', y='rating', data=bank_summary)
plt.title('Average Rating per Bank')
plt.ylabel('Rating')
plt.xlabel('Bank')
plt.savefig('./plots/rating_per_bank.png')
plt.show()

pain_points = {
    'CBE': ['login error', 'slow transfer'],
    'BOA': ['app crashes', 'poor support'],
    'Dashen': ['complex UI', 'long processing times']
}

drivers = {
    'CBE': ['fast navigation', 'modern design'],
    'BOA': ['reliable features', 'clear layout'],
    'Dashen': ['good design', 'secure payments']
}

recommendations = {}

for bank in pain_points:
    recs = []
    if 'login error' in pain_points[bank]:
        recs.append("Implement more robust authentication mechanisms and stress test login endpoints.")
    if 'slow transfer' in pain_points[bank]:
        recs.append("Optimize transaction processing pipelines and monitor server performance.")
    if 'app crashes' in pain_points[bank]:
        recs.append("Implement rigorous QA testing and error monitoring using Sentry or Firebase Crashlytics.")
    if 'poor support' in pain_points[bank]:
        recs.append("Enhance customer support by adding in-app live chat and AI-driven FAQs.")
    if 'complex UI' in pain_points[bank]:
        recs.append("Simplify app design; implement user-centered design principles.")
    if 'long processing times' in pain_points[bank]:
        recs.append("Improve backend processing and implement performance monitoring dashboards.")
    
    # Add feature enhancements based on drivers
    if 'fast navigation' in drivers[bank]:
        recs.append("Continue to invest in intuitive navigation and fast load times.")
    if 'modern design' in drivers[bank]:
        recs.append("Leverage user feedback to refine and modernize UI elements.")
    
    recommendations[bank] = recs

with open('recommendations.md', 'w') as f:
    for bank, recs in recommendations.items():
        f.write(f"### {bank} Recommendations\n")
        for idx, rec in enumerate(recs, 1):
            f.write(f"{idx}. {rec}\n")
        f.write("\n")

