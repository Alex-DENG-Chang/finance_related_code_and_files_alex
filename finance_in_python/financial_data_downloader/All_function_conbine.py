import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from cProfile import label
from matplotlib.pyplot import subplot
import json
import numpy as np

# Inport tricker list
with open(r'/Users/alexdengmbp21/Documents/python_projets/finance_in_python/financial_data_downloader/Tricker/company_tickers.json','r',encoding='UTF-8') as json_file:
    huge_data = json.load(json_file)

# Create a benchmark list
bcm = {'Dow Jones Industrial Average':'^DJI',
       'S&P 500':'^GSPC',
       'NASDAQ Composite':'^IXIC',
       'CAC 40':'^FCHI',
       'Russell 2000(small-cap U.S. stock market)':'^RUT',
       'Hang Seng Index (Hong Kong)':'^HSI',
       'SSE Composite Index ':'000001.SS'
       }

bcm_pd = pd.DataFrame(list(bcm.items()), columns=['Index', 'Ticker'])

# Put json into panda
df_trackers = pd.DataFrame(huge_data)
df_trackers_T = df_trackers.T
print(df_trackers_T)

# Inport the datas ⬆️
# Functions ⬇️

# Serach the tricker
input_string = input("Enter a string to search a stock ticker: ")
search_result = df_trackers_T[df_trackers_T['title'].str.contains(input_string, case=False, na=False)]

# Present the possible trickers
print(search_result)

# Use the index to choose a stock
stock_ticker = int(input("Enter an index (0-based): "))
cik_str_from_user = df_trackers_T.iloc[stock_ticker]['ticker']
print(cik_str_from_user)

# Choose the start and end date
start_day = input('Data start form(YYYY-MM-DD): ')
end_day = input('Data end to (YYYY-MM-DD): ')

# Download the data
stock_data_from_user = yf.download(cik_str_from_user, start=start_day, end=end_day)
stock_data_from_user_transindex=stock_data_from_user.reset_index()

# Ask user if they want to compare with benchmark
compare_with_benchmark = input(print(f"Do you want to compare this stock with a benchmark? (y/n): "))

if compare_with_benchmark.lower() == 'y':
    # Choose the benchmark
    print("\nHere are the available benchmarks:")
    print(bcm_pd)
    benchmark_index = int(input("Enter the index of the benchmark: "))
    benchmark_ticker = bcm_pd.iloc[benchmark_index]['Ticker']

    # Download the data for the benchmark
    benchmark_data = yf.download(benchmark_ticker, start=start_day, end=end_day)
    benchmark_data_transindex = benchmark_data.reset_index()

    # Plot the stock and benchmark together
    x = stock_data_from_user_transindex['Date']
    y1 = stock_data_from_user_transindex['Close']
    y2 = stock_data_from_user_transindex['Volume']
    z1 = benchmark_data_transindex['Close']

    fig, axs = plt.subplots(3, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [2, 1, 2]})

    # Stock close price
    axs[0].plot(x, y1, label='Stock Close Price', color='b')
    axs[0].set_title('Close Price Over Time')
    axs[0].set_ylabel('Price')

    # # Stock trading volume
    axs[1].plot(x, y2, label='Stock Trading Volume', color='b')
    axs[1].set_title('Trading Volume Over Time')
    axs[1].set_ylabel('Volume')

    # Benchmark index
    axs[2].plot(x, z1, label='Index', color='g')
    axs[2].set_title('Index Over Time')
    axs[2].set_ylabel('Index')

    fig.tight_layout()
    plt.show()
else:
    # Plot the stock
    x = stock_data_from_user_transindex['Date']
    y1 = stock_data_from_user_transindex['Close']
    y2 = stock_data_from_user_transindex['Volume']

    fig, axs = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [4, 1]})

    axs[0].plot(x, y1, label='Stock Close Price', color='b')
    axs[0].set_title('Stock Close Price Over Time')
    axs[0].set_ylabel('Price ($)')

    axs[1].plot(x, y2, label='Trading Volume', color='b')
    axs[1].set_title('Trading Volume Over Time')
    axs[1].set_ylabel('Volume')

    fig.tight_layout()
    plt.show()