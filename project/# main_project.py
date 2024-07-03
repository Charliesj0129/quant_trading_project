# main_project.py
from data_collection_preprocessing import collect_market_data, preprocess_data
from train_lstm import train_lstm
from train_random_forest import train_random_forest
from train_dqn import train_dqn
from strategy_adjustment import adjust_strategy
from model_evaluation_with_dqn import evaluate_model
from sentiment_analysis import analyze_sentiments
from report_generation import generate_report
import joblib
import pandas as pd

def main():
    # 數據收集與預處理
    api_url = 'http://example.com/market_data'
    market_data = collect_market_data(api_url)
    preprocessed_data = preprocess_data(market_data)
    preprocessed_data.to_csv('preprocessed_data.csv', index=False)

    # 模型訓練
    lstm_model = train_lstm(preprocessed_data)
    random_forest_model = train_random_forest(preprocessed_data)
    joblib.dump(random_forest_model, 'random_forest_model.pkl')

    # 強化學習訓練
    env_name = 'CartPole-v1'
    train_dqn(env_name)

    # 策略調整
    adjusted_data = adjust_strategy(preprocessed_data, random_forest_model)
    adjusted_data.to_csv('adjusted_data.csv', index=False)

    # 模型評估
    accuracy = evaluate_model(adjusted_data, random_forest_model)
    print(f"Model Accuracy: {accuracy}")

    # 情感分析與報告生成
    news_texts = ["Stock prices are soaring today.", "The market is down."]
    sentiments = analyze_sentiments(news_texts)
    report = generate_report(adjusted_data, sentiments)
    print(report)

if __name__ == "__main__":
    main()