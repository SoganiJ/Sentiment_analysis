import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import nltk
from collections import Counter

nltk.download('punkt')

df = pd.read_csv('D:\VS projects\SentimentAnalysisProject\data\emotion_youtube_comments.csv')

sentiment_column_name = 'emotion' # Change this if needed
sentiment_counts = df[sentiment_column_name].value_counts()

plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, hue=sentiment_counts.index, palette="viridis", legend=False)
plt.title('Sentiment Distribution of YouTube Comments')
plt.xlabel('Sentiment')
plt.ylabel('Number of Comments')
plt.savefig('data/youtube_sentiment_distribution.png')

def generate_wordcloud(text, title, filename):
    if text:  # Check if text is not empty
        wordcloud = WordCloud(width=800, height=400, max_words=150, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(title)
        plt.savefig(filename)
    else:
        print(f"Warning: No text available for {title}. Word cloud not generated.")

positive_tweets = df[df[sentiment_column_name] == 'Positive']['cleaned_tweet'].str.cat(sep=' ')
negative_tweets = df[df[sentiment_column_name] == 'Negative']['cleaned_tweet'].str.cat(sep=' ')

generate_wordcloud(positive_tweets, 'Word Cloud for Positive YouTube Comments', 'data/youtube_positive_wordcloud.png')
generate_wordcloud(negative_tweets, 'Word Cloud for Negative YouTube Comments', 'data/youtube_negative_wordcloud.png')

def plot_top_words(text, title, filename, n=20):
    if text:
        words = nltk.word_tokenize(text)
        word_counts = Counter(words)
        most_common_words = word_counts.most_common(n)
        words, counts = zip(*most_common_words)
        plt.figure(figsize=(12, 6))
        sns.barplot(x=list(counts), y=list(words), palette='coolwarm')
        plt.title(title)
        plt.xlabel('Frequency')
        plt.ylabel('Words')
        plt.tight_layout()
        plt.savefig(filename)
    else:
        print(f"Warning: No text available for {title}. Top words plot not generated.")

plot_top_words(positive_tweets, "Top 20 Most Frequent Words in Positive Comments", "data/top_positive_words.png")
plot_top_words(negative_tweets, "Top 20 Most Frequent Words in Negative Comments", "data/top_negative_words.png")