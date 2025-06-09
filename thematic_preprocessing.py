import pandas as pd 
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv('./data/bank_reviews_with_sentiment.csv')


nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

df['cleaned_review'] = df['review'].apply(preprocess_text)

df.to_csv('./data/bank_reviews_with_cleaned_text.csv', index=False)
print("Text preprocessing completed and saved to bank_reviews_with_cleaned_text.csv")

print("Extracting keywords using TF-IDF...")
all_keywords = {}

for bank in df['bank'].unique():
    bank_reviews = df[df['bank'] == bank]['cleaned_review']
    tfidf = TfidfVectorizer(max_features=20, ngram_range=(1, 2))
    X = tfidf.fit_transform(bank_reviews)
    keywords = tfidf.get_feature_names_out()
    all_keywords[bank] = keywords
    print(f"\nBank: {bank}\nKeywords: {keywords}\n")
    
    
bank_keywords_themes = {
    "Account Access Issues": ["login", "password", "session"],
    "Transaction Performance": ["transfer", "transaction", "slow"],
    "User Interface & Experience": ["design", "layout", "navigation", "ui"],
    "Customer Support": ["support", "contact", "help"],
    "Feature Requests": ["fingerprint", "dark mode"]
}

def assign_theme(review, keyword_theme_map):
    for theme, keywords in keyword_theme_map.items():
        for keyword in keywords:
            if keyword in review:
                return theme
    return "Other"

print("Assigning themes to reviews...")
df['identified_theme'] = df['cleaned_review'].apply(lambda x: assign_theme(x, bank_keywords_themes))

output_file = './data/reviews_with_themes.csv'
df.to_csv(output_file, index=False)
print(f"Analysis complete! Results saved to {output_file}")