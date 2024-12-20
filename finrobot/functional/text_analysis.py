import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download('vader_lexicon', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def analyze_text(text: str) -> str:
    """
    Analyzes the text of a document, performing sentiment analysis and keyword extraction.

    Args:
        text: The text to analyze.

    Returns:
        A string containing the sentiment analysis results and extracted keywords.
    """
    if not text:
        return "No text provided."

    try:
        # Sentiment Analysis
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(text)
        sentiment = "Positive" if sentiment_scores['compound'] > 0 else "Negative" if sentiment_scores['compound'] < 0 else "Neutral"

        # Keyword Extraction
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text.lower())
        words = [word for word in words if word.isalnum() and word not in stop_words]
        word_counts = Counter(words)
        keywords = word_counts.most_common(10)

        results = f"""
        Sentiment: {sentiment}
        Sentiment Scores: {sentiment_scores}
        Keywords: {keywords}
        """
        return results
    except Exception as e:
        return f"An error occurred: {e}"