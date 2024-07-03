# train_lstm.py
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense,Dropout
from sklearn.linear_model import ElasticNet
import numpy as np
import matplotlib.pyplot as plt
import mysql
def train_lstm(data):
    X = data.drop('target', axis=1).values
    y = data['target'].values
    model = Sequential()
    model.add(LSTM(300, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(300))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.add(ElasticNet(alpha=1.0,l1_ratio=0.5))  # Add ElasticNet layer here
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=20, batch_size=32)
    return model

def read_data():

    # Connect to MySQL database

    cnx = mysql.connector.connect(
        host='localhost',
        user='newuser',
        password='Ren-4568357B',
        database='stock_data'
    )

    # Create a cursor object
    cursor = cnx.cursor()

    # Execute the query to fetch the data
    query = "56"
    cursor.execute(query)

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    # Convert the rows into a pandas DataFrame
    data = pd.DataFrame(rows, columns=['column1', 'column2', 'target'])

    return data
# 主程式
if __name__ == "__main__":
    
    train_lstm
