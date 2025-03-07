analyze_sentiment(less) :- positive , negative and neutral comments(will be displayed as quick result on home page)

analyze_sentiment(more) :- all types of emotion (will be shown in DATA column)

same for other MORE and LESS files.

▪️add on for tomorrow :-
1) add emoji pack so that the preprocessed data looks clean
2) changing the naming convention of visualization files


pandas: Provides data structures (like DataFrames) and functions for data manipulation and analysis.

nltk: The Natural Language Toolkit. A suite of libraries for tasks like tokenization, stemming, stopword removal, etc.

textblob: A simplified library for text processing, including basic sentiment analysis.

matplotlib: A plotting library for creating static, interactive, and animated visualizations in Python.

wordcloud: A library for generating word clouds from text data.

seaborn: A data visualization library based on Matplotlib. It provides a high-level interface for creating informative and attractive statistical graphics.

google-api-python-client: The official Google API client library for Python. Used for interacting with the YouTube Data API.

▪️Tech stack :- 

Programming Language:

Python → Core language for data processing, machine learning, and visualization.
Data Handling & Processing:

Pandas → Handles and processes large datasets (YouTube comments).
NLTK & TextBlob → Cleans, tokenizes, and prepares text data.
NRCLex → Extracts emotions from text.

Machine Learning & AI:
Transformers (Hugging Face) → Uses a pre-trained RoBERTa model (SamLowe/roberta-base-go_emotions) for emotion detection.


Visualization & Analytics:
Matplotlib → Creates bar charts, pie charts, and data visualizations.
WordCloud → Generates word clouds for commonly used words in different emotions.

Data Storage & Management:
CSV Files (Pandas) → Stores processed comments, emotions, and results.

[Social Media APIs (Meta, YouTube, Reddit, X (Twitter))]
      |
      V
[Data Collection Modules (Python Scripts using API libraries)]  (data_collection.py)
      |
      V
[Data Storage (Cloud Storage: AWS S3, Google Cloud Storage, Azure Blob Storage)]
      |
      V
[Data Preprocessing & Sentiment Analysis (Python: Pandas, NLTK/SpaCy, Transformers)]  (sentiment_analysis.py)
      |
      V
[Data Visualization (Python: Matplotlib, Seaborn, Plotly, Dash)] (visualization.py)
      |
      V
[Conclusion Generation (Python: Natural Language Generation - Fine-tuned LLM or Rules-Based)] (conclusion_generation.py)
      |
      V
[Excel Output (Python: Pandas)] (excel_export.py)
      |
      V
[Web Application (Optional: Flask, Django, Streamlit)] (app.py)
          |
          V
      [User Interface (HTML, CSS, JavaScript)]
