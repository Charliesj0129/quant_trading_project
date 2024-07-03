# report_generation.py
from transformers import pipeline

def generate_report(data, sentiments):
    report_generator = pipeline('text-generation', model='gpt-3.5-turbo')
    report = f"資產報告：\n\n"
    report += f"數據摘要：\n{data.describe()}\n\n"
    report += f"情感分析：\n{sentiments}\n\n"
    report += "根據最新的數據和情感分析，我們對市場進行如下展望...\n"
    generated_text = report_generator(report, max_length=500)
    return generated_text[0]['generated_text']

# 主程式
if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv('adjusted_data.csv')
    news_texts = ["Stock prices are soaring today.", "The market is down."]
    from sentiment_analysis import analyze_sentiments
    sentiments = analyze_sentiments(news_texts)
    report = generate_report(data, sentiments)
    print(report)