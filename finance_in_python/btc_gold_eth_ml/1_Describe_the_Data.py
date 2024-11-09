import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
import seaborn as sns
import statsmodels as sm

all_in_one = pd.read_excel(r'/Users/alexdengmbp21/Desktop/Fall 24/Master_Thesis/Adjusted_Data/GOLD_BTC_ETH_VIX_Nor.xlsx', index_col='Week')


gold_close_df = all_in_one['Gold Close']
gold_close_nor_df = all_in_one['Gold Close Nor']

btc_close_df = all_in_one['BTC Close']
btc_close_nor_df = all_in_one['BTC Close Nor']

eth_close_df = all_in_one['ETH Close']
eth_close_nor_df = all_in_one['ETH Close Nor']

vix_close_df = all_in_one['VIX Close']
vix_close_nor_df = all_in_one['VIX Close Nor']





# Plots ——————————————————————————————————————————————————————————————————————————————————————————————————
gold_close_df.plot(label='Gold Price', legend=True)
btc_close_df.plot(label='BTC Price', legend=True, secondary_y=True)
plt.show()

gold_close_nor_df.plot(legend=True, color='y')
btc_close_nor_df.plot(legend=True, color='r')
eth_close_nor_df.plot(legend=True, color='b')
plt.show()

gold_close_df.plot(legend=True)
vix_close_df.plot(legend=True, secondary_y=True)
plt.show
# Plots ——————————————————————————————————————————————————————————————————————————————————————————————————





# Corr ——————————————————————————————————————————————————————————————————————————————————————————————————
# non_nor_dict = {
#     'Gold': gold_close_df,
#     'BTC': btc_close_df,
#     'ETH': eth_close_df,
#     'VIX': vix_close_df,}
#
# nor_dict = {
#     'Gold': gold_close_nor_df,
#     'BTC': btc_close_nor_df,
#     'ETH': eth_close_nor_df,
#     'VIX': vix_close_nor_df,}

# df_non_nor = pd.DataFrame(non_nor_dict)
# corr_non_nor = df_non_nor.corr()
# sns.heatmap(corr_non_nor, annot=True)
# plt.show()

# df_nor = pd.DataFrame(nor_dict)
# corr_nor = df_nor.corr()
# sns.heatmap(corr_nor, annot=True)
# plt.show()
# Corr ——————————————————————————————————————————————————————————————————————————————————————————————————
