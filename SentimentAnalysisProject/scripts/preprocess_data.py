import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')  # Download stopwords if you haven't already

# Load the CSV
try:
    df = pd.read_csv('data/youtube_comments.csv')
except FileNotFoundError:
    print("Error: data/youtube_comments.csv not found.  Make sure to run collect_youtube_comments.py first.")
    exit()

# Rename the comment column to "Tweet"
df = df.rename(columns={"Comment": "Tweet"})

# If the dataframe does not have the column 'Tweet', raise error
if 'Tweet' not in df.columns:
    raise ValueError("The DataFrame does not contain a 'Tweet' column.")

# Handle missing values: Fill NaN with empty strings
df['Tweet'] = df['Tweet'].fillna('')

def clean_text(text):
    """Cleans the input text by removing URLs, mentions, hashtags,
    special characters, and converting to lowercase.
    """
    if not isinstance(text, str):  # added check
        return ""  # Return empty string if not string

    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove mentions (@username)
    text = re.sub(r'@\w+', '', text)
    # Remove hashtags
    text = re.sub(r'#\w+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

df['cleaned_tweet'] = df['Tweet'].apply(clean_text)

# Remove Stopwords
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    """Removes stop words from the input text."""
    if not isinstance(text, str):  # Ensure text is a string
        return ""
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

df['cleaned_tweet'] = df['cleaned_tweet'].apply(remove_stopwords)

print(df.head())
df.to_csv('data/cleaned_youtube_comments.csv', index=False)