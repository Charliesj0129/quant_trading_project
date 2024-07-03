# train_random_forest.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_random_forest(data):
    X = data.drop('target', axis=1)
    y = data['target']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

# 主程式
if __name__ == "__main__":
    data = pd.read_csv('preprocessed_data.csv')
    model = train_random_forest(data)
    import joblib
    joblib.dump(model, 'random_forest_model.pkl')
