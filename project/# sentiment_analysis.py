# sentiment_analysis.py
from transformers import pipeline

def analyze_sentiments(news_texts):
    classifier = pipeline('sentiment-analysis')
    results = classifier(news_texts)
    return results

# 主程式
if __name__ == "__main__":
    news_texts = ["Stock prices are soaring today.", "The market is down."]
    sentiments = analyze_sentiments(news_texts)
    print(sentiments)