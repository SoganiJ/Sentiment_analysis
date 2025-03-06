import pandas as pd
from transformers import pipeline

# Load the CSV
try:
    df = pd.read_csv('data/cleaned_youtube_comments.csv')
except FileNotFoundError:
    print("Error: data/cleaned_youtube_comments.csv not found. Make sure to run preprocess_data.py first.")
    exit()

# Handle missing values: Fill NaN with empty strings
df['cleaned_tweet'] = df['cleaned_tweet'].fillna('')

# Load the emotion detection pipeline
emotion_pipeline = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", return_all_scores=True)

def get_emotions(text):
    """
    Detects emotions in the given text using a pre-trained transformer model.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary containing the probabilities for each emotion category.
    """
    if not isinstance(text, str):
        return {}

    try:
        # Run the emotion detection pipeline
        emotion_results = emotion_pipeline(text)

        # Extract the emotion labels and scores from the pipeline output
        emotion_scores = {d['label']: d['score'] for d in emotion_results[0]}
        return emotion_scores
    except Exception as e:
        print(f"An error occurred during emotion detection: {e}")
        return {}

# Apply emotion detection to each cleaned tweet
df['emotions'] = df['cleaned_tweet'].apply(get_emotions)

# Find the most probable emotion
def get_dominant_emotion(emotions):
    if not emotions:
        return 'Neutral'  # Or 'Unknown'
    return max(emotions, key=emotions.get)


df['dominant_emotion'] = df['emotions'].apply(get_dominant_emotion)

print(df.head())
df.to_csv('data/emotion_youtube_comments(more).csv', index=False)