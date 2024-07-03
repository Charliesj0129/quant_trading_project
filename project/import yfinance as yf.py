import yfinance as yf
stock_data = yf.download("030063.TW",period='1d')
print(stock_data)