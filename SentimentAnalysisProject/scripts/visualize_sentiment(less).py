import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv('data/emotion_youtube_comments(less).csv')

# Sentiment Distribution
sentiment_counts = df['sentiment'].value_counts()
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of YouTube Comments')  # Changed label
plt.savefig('data/youtube_sentiment_distribution.png')

# Word Cloud for Positive Tweets
positive_tweets = df[df['sentiment'] == 'Positive']['cleaned_tweet'].str.cat(sep=' ')
wordcloud = WordCloud(width=800, height=400, max_words=100, background_color='white').generate(positive_tweets)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Positive YouTube Comments')  # Changed title
plt.savefig('data/youtube_positive_wordcloud.png')

# Word Cloud for Negative Tweets
negative_tweets = df[df['sentiment'] == 'Negative']['cleaned_tweet'].str.cat(sep=' ')
wordcloud = WordCloud(width=800, height=400, max_words=100, background_color='white').generate(negative_tweets)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Negative YouTube Comments')  # Changed title
plt.savefig('data/youtube_negative_wordcloud.png')

print("file is saved nigga")