import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
import seaborn as sns
import statsmodels.api as sm
import numpy as np

all_in_one = pd.read_excel(r'/Users/alexdengmbp21/Desktop/Fall 24/Master_Thesis/Adjusted_Data/GOLD_BTC_ETH_VIX_Nor_after2017.xlsx', index_col='Week')


gold_close_df = all_in_one['Gold Close']
gold_close_nor_df = all_in_one['Gold Close Nor']

btc_close_df = all_in_one['BTC Close']
btc_close_nor_df = all_in_one['BTC Close Nor']

eth_close_df = all_in_one['ETH Close']
eth_close_nor_df = all_in_one['ETH Close Nor']

vix_close_df = all_in_one['VIX Close']
vix_close_nor_df = all_in_one['VIX Close Nor']




# OLS (BTC : GOLD)——————————————————————————————————————————————————————————————————————————————————————————————————
features = gold_close_nor_df
targets = btc_close_nor_df

features = pd.DataFrame({
    'Gold Close': gold_close_nor_df,
    'VIX Close': vix_close_nor_df,
    'ETH Close': eth_close_nor_df
})

targets = btc_close_nor_df



# No cut ⬇
# linear_features = sm.add_constant(features)
# model = sm.OLS(targets, linear_features)
# results = model.fit()
# print(results.summary())

# Cut ⬇
linear_features = sm.add_constant(features)
train_size = int(0.85 * targets.shape[0])
train_features = linear_features[:train_size]
train_targets = targets[:train_size]
test_features = linear_features[train_size:]
test_targets = targets[train_size:]

model = sm.OLS(train_targets, train_features)
results = model.fit()
print(results.summary())

train_predictions = results.predict(train_features)
test_predictions = results.predict(test_features)

# Scatter the predictions vs the targets with 20% opacity
plt.scatter(train_predictions, train_targets, alpha=0.2, color='b', label='train')
plt.scatter(test_predictions, test_targets, alpha=0.2, color='r', label='test')

# Plot the perfect prediction line
xmin, xmax = plt.xlim()
plt.plot(np.arange(xmin, xmax, 0.01), np.arange(xmin, xmax, 0.01), c='k')

# Set the axis labels and show the plot
plt.xlabel('predictions')
plt.ylabel('actual')
plt.legend()  # show the legend
plt.show()

# OLS (BTC : GOLD)——————————————————————————————————————————————————————————————————————————————————————————————————





# OLS (BTC : GOLD, VIX)——————————————————————————————————————————————————————————————————————————————————————————————————
# features = pd.DataFrame({
#     'Gold Close': gold_close_nor_df,
#     'VIX Close': vix_close_nor_df
# })

# targets = btc_close_nor_df

# linear_features = sm.add_constant(features)

# model = sm.OLS(targets, linear_features)
# results = model.fit()
# print(results.summary())
# OLS (BTC : GOLD, VIX)——————————————————————————————————————————————————————————————————————————————————————————————————

