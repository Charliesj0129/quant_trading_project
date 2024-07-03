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
api = sj.Shioaji()

def login(api):
    
    api.login(
        api_key="3gNpFbPDW3YC7RhKzXRthtDJ2TDkkuevvNuqsq1Jese2",
        secret_key="NbHaa8brgXNmsckwvXLtCnrgCfBWKumrUbXyNgqsWXK",
    )
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
            # 獲取股票分紅信息

            # 獲取股票持有人信息
            holders = stock._holders
            print("股票持有人信息:")
            print(holders)

            # 獲取股票行動信息
            actions = stock.actions
            print("股票行動信息:")
            print(actions)

            # 獲取股票日曆信息
            calendar = stock.calendar
            print("股票日曆信息:")
            print(calendar)

            # 獲取股票拆分信息
            splits = stock.splits
            print("股票拆分信息:")
            print(splits)
            
            
           
            

            
login(api)
collect_stock_fundamental_data(api)
