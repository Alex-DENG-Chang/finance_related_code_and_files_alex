import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
import seaborn as sns
import statsmodels.api as sm
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# —————————————————————————————————————————————————————— data prepare ——————————————————————————————————————————————————————————————————————————————————————————————————
all_in_one = pd.read_excel(r'/Users/alexdengmbp21/Desktop/Fall 24/Master_Thesis/Adjusted_Data/GOLD_BTC_ETH_VIX_Nor_after2017.xlsx', index_col='Week')
print(all_in_one)

gold_close_df = all_in_one['Gold Close']
gold_close_nor_df = all_in_one['Gold Close Nor']

btc_close_df = all_in_one['BTC Close']
btc_close_nor_df = all_in_one['BTC Close Nor']

eth_close_df = all_in_one['ETH Close']
eth_close_nor_df = all_in_one['ETH Close Nor']

vix_close_df = all_in_one['VIX Close']
vix_close_nor_df = all_in_one['VIX Close Nor']


features = gold_close_nor_df
targets = btc_close_nor_df
linear_features = sm.add_constant(features)
train_size = int(0.85 * targets.shape[0])
train_features = linear_features[:train_size]
train_targets = targets[:train_size]
test_features = linear_features[train_size:]
test_targets = targets[train_size:]
# —————————————————————————————————————————————————————— data prepare ——————————————————————————————————————————————————————————————————————————————————————————————————






# —————————————————————————————————————————————————————— KNN ——————————————————————————————————————————————————————————————————————————————————————————————————
for n in range(2, 13):
    # Create and fit the KNN model
    knn = KNeighborsRegressor(n_neighbors=n)

    # Fit the model to the training data
    knn.fit(train_features, train_targets)

    # Print number of neighbors and the score to find the best value of n
    print("n_neighbors =", n)
    print('train, test scores')
    print(knn.score(train_features, train_targets))
    print(knn.score(test_features, test_targets))
    print()  # prints a blank line

knn = KNeighborsRegressor(n_neighbors=6)

# Fit the model
knn.fit(train_features, train_targets)

# Get predictions for train and test sets
train_predictions = knn.predict(train_features)
test_predictions = knn.predict(test_features)

# Plot the actual vs predicted values
plt.scatter(train_predictions, train_targets, label='train')
plt.scatter(test_predictions, test_targets, label='test')
plt.legend()
plt.show()
# —————————————————————————————————————————————————————— KNN ——————————————————————————————————————————————————————————————————————————————————————————————————
