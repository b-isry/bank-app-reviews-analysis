# Bank App Review Analysis

This project focuses on analyzing customer reviews for various bank applications. It includes Python scripts for scraping reviews, preprocessing text data, performing sentiment analysis, and conducting thematic analysis to identify key topics and features discussed by users.

## Project Structure

```
bank-app-reviews-analysis/
├── data/
│   ├── bank_reviews.csv
│   ├── bank_reviews_cleaned.csv
│   ├── bank_reviews_with_sentiment.csv
│   ├── bank_reviews_with_cleaned_text.csv
│   ├── reviews_with_themes.csv
│   └── sentiment_summary.csv
├── scripts/
│   ├── scrape_reviews.py
│   ├── preprocess_reviews.py
│   ├── sentiment_vader.py
│   └── thematic_preprocessing.py
├── requirements.txt
└── README.md
```

## Scripts

-   `scripts/scrape_reviews.py`: This script is responsible for collecting app reviews from sources like the Google Play Store (inferred from `google-play-scraper` in `requirements.txt`).
-   `scripts/preprocess_reviews.py`: This script handles initial data cleaning and preprocessing steps on the raw reviews.
-   `scripts/sentiment_vader.py`: This script performs sentiment analysis on the reviews, using the VADER (Valence Aware Dictionary and sEntiment Reasoner) tool to classify reviews as positive, negative, or neutral.
-   `scripts/thematic_preprocessing.py`: This script performs text preprocessing tailored for thematic analysis. It cleans the review text by converting to lowercase, removing non-alphabetic characters, lemmatizing words using spaCy, and removing stop words. It then extracts keywords using TF-IDF and assigns predefined themes to the reviews based on these keywords.

## Data Files

The `data/` directory contains various CSV files generated throughout the analysis pipeline:

-   `bank_reviews.csv`: Contains the raw reviews, as scraped by `scrape_reviews.py`.
-   `bank_reviews_cleaned.csv`: Contains reviews after an initial cleaning phase, possibly from `preprocess_reviews.py`.
-   `bank_reviews_with_sentiment.csv`: Contains the reviews along with their calculated sentiment scores and labels (e.g., positive, negative, neutral) from `sentiment_vader.py`. This file is used as input for `thematic_preprocessing.py`.
-   `bank_reviews_with_cleaned_text.csv`: Contains the review text after being processed by `thematic_preprocessing.py` (lowercased, punctuation removed, lemmatized, stop words removed).
-   `reviews_with_themes.csv`: The final output file from `thematic_preprocessing.py`, containing the reviews along with their assigned themes (e.g., "Account Access Issues", "Feature Requests").
-   `sentiment_summary.csv`: contains a summarized view of the sentiment analysis results across different banks or categories.

## Setup and Installation

1.  **Clone the repository (if applicable) or ensure you have the project files.**
2.  **Install Python dependencies:**
    Navigate to the project root directory in your terminal and run:
    ```powershell
    pip install -r requirements.txt
    ```
    The `requirements.txt` file includes:
    -   `google-play-scraper`
    -   `pandas`
    -   `numpy`
    -   `vaderSentiment`
    -   `scikit-learn`
    -   `spacy`
    you can install them via pip:
    ```powershell
    pip install spacy scikit-learn
    ```

3.  **Download spaCy language model:**
    The `thematic_preprocessing.py` script uses the `en_core_web_sm` model from spaCy. Download it by running:
    ```powershell
    python -m spacy download en_core_web_sm
    ```

## Running the Analysis

The scripts in the `scripts/` directory are designed to be run sequentially or individually, depending on the analysis stage.

For example, to run the thematic preprocessing and theme assignment script:
```powershell
python scripts/thematic_preprocessing.py
```
This script will:
1.  Load reviews from `data/bank_reviews_with_sentiment.csv`.
2.  Preprocess the 'review' column:
    *   Convert text to lowercase.
    *   Remove non-alphabetic characters.
    *   Lemmatize tokens using spaCy (excluding stop words and punctuation).
3.  Save the DataFrame with the new `cleaned_review` column to `data/bank_reviews_with_cleaned_text.csv`.
4.  Extract the top 20 TF-IDF keywords (unigrams and bigrams) for each bank from the `cleaned_review`.
5.  Assign themes to each review based on a predefined dictionary of keywords associated with themes such as "Account Access Issues", "Transaction Performance", "User Interface & Experience", "Customer Support", and "Feature Requests".
6.  Save the final DataFrame, including the `identified_theme` column, to `data/reviews_with_themes.csv`.


