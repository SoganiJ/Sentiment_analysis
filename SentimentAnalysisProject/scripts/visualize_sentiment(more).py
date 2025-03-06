import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib

# Use non-interactive backend (for server compatibility)
matplotlib.use('Agg')

# Load the CSV
try:
    df = pd.read_csv('data/emotion_youtube_comments(more).csv')
except FileNotFoundError:
    print("Error: data/emotion_youtube_comments.csv not found. Make sure to run analyze_sentiment.py first.")
    exit()

# Check if required columns exist
if 'dominant_emotion' not in df.columns or 'cleaned_tweet' not in df.columns:
    print("Error: The DataFrame must contain 'dominant_emotion' and 'cleaned_tweet' columns.")
    exit()

# Emotion Distribution - Horizontal Bar Plot
emotion_counts = df['dominant_emotion'].value_counts()
plt.figure(figsize=(10, 6))
emotion_counts.sort_values().plot(kind='barh', color='skyblue')
plt.title('Distribution of Emotions in YouTube Comments')
plt.xlabel('Number of Comments')
plt.ylabel('Emotion')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('data/youtube_emotion_distribution.png')

# Pie Chart of Emotion Distribution
plt.figure(figsize=(8, 8))
emotion_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Emotion Distribution in YouTube Comments')
plt.ylabel('')  # Hide y-label for better appearance
plt.savefig('data/youtube_emotion_piechart.png')

# Generate Word Clouds for the Top 3 Emotions
top_emotions = emotion_counts.index[:3]  # Get the 3 most common emotions

for emotion in top_emotions:
    emotion_text = df[df['dominant_emotion'] == emotion]['cleaned_tweet'].str.cat(sep=' ')
    wordcloud = WordCloud(width=800, height=400, max_words=100, background_color='white').generate(emotion_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud for {emotion} Comments')
    plt.savefig(f'data/youtube_{emotion.lower()}_wordcloud.png')

print("✅ Visualization(more) saved successfully!")

