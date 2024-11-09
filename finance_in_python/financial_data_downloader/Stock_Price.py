import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


stock_A = input('The Code of the stock: ' )
start_day = input('Data start form(YYYY-MM-DD): ')
end_day = input('Data end to (YYYY-MM-DD): ')

stock_name = yf.download(stock_A, start=start_day, end=end_day)

stock_name.to_excel(f'/Users/alexdengmbp21/Desktop/{stock_A} Stock price from {start_day} to {end_day}.xlsx', sheet_name=stock_A, index=True)