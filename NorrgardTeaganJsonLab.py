#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:38:42 2022

@author: teagannorrgard
"""

import json
import requests


stocks = input("What stocks do you want the price of? tickers:")
tick_list = stocks.split(',')

url = "https://yfapi.net/v6/finance/quote?region=US&lang=en&symbols=AAPL%2CBTC-USD%2CEURUSD%3DX"
headers = {'x-api-key': "tvRC07MKWp5IsIRMH9dal20CknoctNjv9cdn2LlN"}

names = []
prices = []

for ticker in tick_list:
    ticker = ticker.upper()
    querystring = {"symbols":ticker}
    response = requests.request("GET", url, headers=headers, params=querystring)
    stock_json = response.json()
    
    name = stock_json['quoteResponse']['result'][0]['displayName']
    price = stock_json['quoteResponse']['result'][0]['regularMarketPrice']
    
    names.append(name)
    prices.append(price)


for i in range(len(names)):
    print(str(names[i]) + ": " + str(prices[i]))