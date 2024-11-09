from cProfile import label
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot

ateyy_all = pd.read_excel(r'/Users/alexdengmbp21/Desktop/Fall 24/VALUATION/ATEYY/ATEYY Stock price from 2001-09-18 to 2024-06-30.xlsx')
print(ateyy_all.head())
nasdaq_match = pd.read_excel(r'/Users/alexdengmbp21/Desktop/Fall 24/VALUATION/ATEYY/^IXIC Stock price from 2001-09-18 to 2024-06-30.xlsx')
print(nasdaq_match)

x = ateyy_all['Date']
y1 = ateyy_all['Close']
y2 = ateyy_all['Volume']
y3 = nasdaq_match['Close']


fig, axs = plt.subplots(3, 1, figsize=(8,6), gridspec_kw={'height_ratios': [2, 1,2 ]})

# Plot Close line on the first subplot (top)
axs[0].plot(x, y1, label='Close Price', color='b')
axs[0].set_title('Advantest Corp Stock Price Over Time')
axs[0].set_ylabel('Price ($)')

# Plot Trading Volume line on the second subplot
axs[1].plot(x, y2, label='Trading Volume', color='b')
axs[1].set_title('Advantest Corp Trading Volume Over Time')
axs[1].set_ylabel('Volume (units)')

#plot thrid one
axs[2].plot(x, y3, label='Nadaq Index', color='g')
axs[2].set_title('Nasdaq Index Over Time')
axs[2].set_ylabel('Index')

# Layout so plots do not overlap
fig.tight_layout()
plt.show()
