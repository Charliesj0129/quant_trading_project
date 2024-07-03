# data_collection_preprocessing.py
import pandas as pd
import pymysql
import requests
import shioaji as sj
from shioaji import contracts
import pandas as pd
import requests
import shioaji as sj
from shioaji import contracts
import yfinance as yf
from pymongo import MongoClient
import datetime
import time
from sqlalchemy import create_engine

# Login to Shioaji
api = sj.Shioaji()

def login(api):
    
    api.login(
        api_key="3gNpFbPDW3YC7RhKzXRthtDJ2TDkkuevvNuqsq1Jese2",
        secret_key="NbHaa8brgXNmsckwvXLtCnrgCfBWKumrUbXyNgqsWXK",
    )

def collect_stock_data(api,start_date,end_date):
    contracts = api.Contracts.Stocks.TSE
    all_data = pd.DataFrame()
    
    for contract_code in dir(contracts):
        # 跳過內建屬性
        if contract_code.startswith("__"):
            continue
        # 只處理 TSE 開頭的合同
        if "TSE" in contract_code:
            contract_attr = getattr(contracts, contract_code)
            contract_symbol = str(contract_attr.code)
            
            kbars = api.kbars(
                contract = api.Contracts.Stocks.TSE[contract_symbol],
                start = start_date,
                end = end_date
            )
            df = pd.DataFrame({**kbars})
            df['contract_symbol'] = contract_symbol
            df.ts = pd.to_datetime(df.ts)
            time.sleep(10)
            if df is None :
                api.logout()
                time(10)
                login(api)
                try:
                    kbars = api.kbars(
                        contract=contract_symbol,
                        start=start_date,
                        end=end_date
                    )
                    df = pd.DataFrame({**kbars})
                    df.ts = pd.to_datetime(df.ts)

                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
            save_to_MySQL_stock(df_stock=df)
    
                
def collect_index_data(api,start_date,end_date):
    contracts = api.Contracts.Indexs.TSE
    all_data = []
    
    for contract_code in dir(contracts):
        # 跳過內建屬性
        if contract_code.startswith("__"):
            continue
        # 只處理 TSE 開頭的合同
        if "TSE" in contract_code:
            contract_attr = getattr(contracts, contract_code)
            contract_symbol = str(contract_attr.symbol)
            index_data = api.kbars(
                contract = contract_symbol,
                start = start_date,
                end = end_date
            )
            time.sleep(10)
            if index_data is None :
                api.logout()
                time(10)
                login(api)
                try:
                    index_data = api.kbars(
                        contract=contract_symbol,
                        start=start_date,
                        end=end_date
                    )
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
    return index_data

def collect_otc_data(api,start_date,end_date):
    contracts = api.Contracts.Stocks.OTC
    all_data = []
    
    for contract_code in dir(contracts):
        # 跳過內建屬性
        if contract_code.startswith("__"):
            continue
        # 只處理 TSE 開頭的合同
        if "TSE" in contract_code:
            contract_attr = getattr(contracts, contract_code)
            contract_symbol = contract_attr.symbol
            otc_data = api.kbars(
                contract = contract_symbol,
                start = start_date,
                end = end_date
            )
            time.sleep(10)
            if otc_data is None :
                api.logout()
                time(10)
                login(api)
                try:
                    otc_data = api.kbars(
                        contract=contract_symbol,
                        start=start_date,
                        end=end_date
                    )
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
    return otc_data

def collect_stock_fundamental_data (api):
    contracts = api.Contracts.Stocks.TSE
    all_data = pd.DataFrame()
    
    for contract_code in dir(contracts):
        # 跳過內建屬性
        if contract_code.startswith("__") or "TSE" in contract_code:
            contract_attr = getattr(contracts, contract_code)
            contract_symbol = str(contract_attr.code)
            ticker = contract_symbol+".TW"
            # 獲取股票基本資料
            stock = yf.Ticker(ticker)

            # 獲取公司基本面資料
            info = stock.info
            print("公司名稱:", info.get('longName'))
            print("行業:", info.get('industry'))
            print("市值:", info.get('marketCap'))
            print("市盈率:", info.get('trailingPE'))
            print("每股收益:", info.get('epsTrailingTwelveMonths'))

            # 獲取財務報表
            financials = stock.financials
            print("財務報表:")
            print(financials)

            # 獲取資產負債表
            balance_sheet = stock.balance_sheet
            print("資產負債表:")
            print(balance_sheet)

            # 獲取現金流量表
            cashflow = stock.cashflow
            print("現金流量表:")
            print(cashflow)

            # 獲取最近一次的分析師建議
            recommendations = stock.recommendations
            print("分析師建議:")
            print(recommendations)

            # 獲取最近一次的財報數據
            earnings = stock.earnings
            print("最近財報數據:")
            print(earnings)

def collect_future_data(api,start_date,end_date):
    contracts = api.Contracts.Futures.TXF
    all_data = []
    
    for contract_code in dir(contracts):
        # 跳過內建屬性
        if contract_code.startswith("__"):
            continue
        # 只處理 TXF 開頭的合同
        if "TXF" in contract_code:
            contract_attr = getattr(contracts, contract_code)
            contract_symbol = contract_attr.symbol
            future_data = api.kbars(
                contract = contract_symbol,
                start = start_date,
                end = end_date
            )
            time.sleep(10)
            if future_data is None :
                api.logout()
                time(10)
                login(api)
                try:
                    future_data = api.kbars(
                        contract=contract_symbol,
                        start=start_date,
                        end=end_date
                    )
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
    return future_data
   
    
def save_to_MySQL_stock(df_stock):
    # Connect to MySQL
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user = 'newuser',
        passwd = 'Ren-4568357B',
        db = 'stock_data'
    )

def save_to_MySQL_index(df_index):
    # Connect to MySQL
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user = 'newuser',
        passwd = 'Ren-4568357B',
        db = 'index_data'
    )

def save_to_MySQL_future(df_future):
    # Connect to MySQL
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user = 'newuser',
        passwd = 'Ren-4568357B',
        db = 'future_data'
    )

#cleaning data
def fill_missing_data(df):
    # Fill missing data
    df = df.fillna(method='ffill')
    df = df.fillna(method='bfill')
    return df

# 主程式
if __name__ == "__main__":
    login(api)
    collect_stock_data(api,'2021-06-30','2024-07-02')
    #save_to_MySQL_stock(df_stock)
    #df_index = collect_index_data()
    #save_to_MySQL_index(df_index)
    #df_future = collect_future_data()
    #save_to_MySQL_future(df_future)

    