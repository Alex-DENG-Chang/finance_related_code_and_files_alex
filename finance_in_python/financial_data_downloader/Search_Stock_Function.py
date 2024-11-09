import json

import pandas as pd

with open(r'/Users/alexdengmbp21/Documents/Python_Projets/Finance_data_downloader/Tricker/company_tickers.json','r',encoding='UTF-8') as json_file:
    huge_data = json.load(json_file)

df_trackers = pd.DataFrame(huge_data)
df_trackers_T = df_trackers.T
print(df_trackers_T)

input_string = input("Enter a string to search a stock ticker: ")
search_result = df_trackers_T[df_trackers_T['title'].str.contains(input_string, case=False, na=False)]

print(search_result)

stock_ticker = int(input("Enter an index (0-based): "))
cik_str_from_user = df_trackers_T.iloc[stock_ticker]['cik_str']
print(cik_str_from_user)