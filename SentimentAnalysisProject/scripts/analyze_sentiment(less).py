import pandas as pd
from textblob import TextBlob

df = pd.read_csv('data/cleaned_youtube_comments.csv')

# Handle missing values: Fill NaN with empty strings
df['cleaned_tweet'] = df['cleaned_tweet'].fillna('')

def get_sentiment(text):
    if not isinstance(text, str): #Added check
        return 0.0 #Return neutral sentiment if not string
    analysis = TextBlob(text)
    # Return sentiment polarity: -1 (negative) to 1 (positive)
    return analysis.sentiment.polarity

df['sentiment_score'] = df['cleaned_tweet'].apply(get_sentiment)

# Categorize sentiment
def categorize_sentiment(score):
    if score > 0.1:  # Tune this threshold
        return 'Positive'
    elif score < -0.1:  # Tune this threshold
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['sentiment_score'].apply(categorize_sentiment)

print(df.head())
df.to_csv('data/emotion_youtube_comments(less).csv', index=False)