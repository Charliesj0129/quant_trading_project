# model_evaluation_with_dqn.py
import pandas as pd
from sklearn.metrics import accuracy_score

def evaluate_model(data, model):
    X = data.drop('target', axis=1)
    y_true = data['target']
    y_pred = model.predict(X)
    accuracy = accuracy_score(y_true, y_pred)
    return accuracy

# 主程式
if __name__ == "__main__":
    data = pd.read_csv('adjusted_data.csv')
    import joblib
    model = joblib.load('random_forest_model.pkl')
    accuracy = evaluate_model(data, model)
    print(f"Model Accuracy: {accuracy}")