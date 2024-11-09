import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
import seaborn as sns
import statsmodels.api as sm
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import ParameterGrid
from sklearn.ensemble import GradientBoostingRegressor




# —————————————————————————————————————————————————————— data preperation ——————————————————————————————————————————————————————————————————————————————————————————————————
all_in_one = pd.read_excel(r'/Users/alexdengmbp21/Desktop/Fall 24/Master_Thesis/Adjusted_Data/GOLD_BTC_ETH_VIX_Nor.xlsx', index_col='Week')
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
# —————————————————————————————————————————————————————— data preperation ——————————————————————————————————————————————————————————————————————————————————————————————————






# —————————————————————————————————————————————————————— decision tree ——————————————————————————————————————————————————————————————————————————————————————————————————
# decision_tree = DecisionTreeRegressor(max_depth=10)
# decision_tree.fit(train_features, train_targets)
# print(decision_tree.score(train_features, train_targets))
# print(decision_tree.score(test_features, test_targets))
#
# train_predictions = decision_tree.predict(train_features)
# test_predictions = decision_tree.predict(test_features)
# plt.scatter(train_predictions, train_targets, label='train')
# plt.scatter(test_predictions, test_targets, label='test')
# plt.legend()
# plt.show()
# —————————————————————————————————————————————————————— decision tree ——————————————————————————————————————————————————————————————————————————————————————————————————







# —————————————————————————————————————————————————————— decision tree loops ——————————————————————————————————————————————————————————————————————————————————————————————————
# for d in [3,5,10]:
#     decision_tree = DecisionTreeRegressor(max_depth = d)
#     decision_tree.fit(train_features, train_targets)
#
#     print('max_depth=', str(d))
#     print(decision_tree.score(train_features, train_targets))
#     print(decision_tree.score(test_features, test_targets), '\n')
# —————————————————————————————————————————————————————— decision tree loops ——————————————————————————————————————————————————————————————————————————————————————————————————





# —————————————————————————————————————————————————————— random forest ——————————————————————————————————————————————————————————————————————————————————————————————————
rfr_gold_btc_nor = RandomForestRegressor(n_estimators=200)
rfr_gold_btc_nor.fit(train_features, train_targets)


# Create a dictionary of hyperparameters to search
grid = {'n_estimators': [200], 'max_depth': [3], 'max_features': [4, 8], 'random_state': [42]}
train_scores = []
test_scores = []

# Loop through the parameter grid, set the hyperparameters, and save the scores
for g in ParameterGrid(grid):
    rfr_gold_btc_nor.set_params(**g)  # ** is "unpacking" the dictionary
    rfr_gold_btc_nor.fit(train_features, train_targets)
    test_scores.append(rfr_gold_btc_nor.score(test_features, test_targets))
    train_scores.append(rfr_gold_btc_nor.score(train_features, train_targets))

# Find best hyperparameters from the test score and print
best_idx = np.argmax(test_scores)
print('Train score: ',train_scores[best_idx], ParameterGrid(grid)[best_idx])
print('Test score: ',test_scores[best_idx], ParameterGrid(grid)[best_idx])

# -1.573860986438378 {'random_state': 42, 'n_estimators': 200, 'max_features': 4, 'max_depth': 3}

rfr_gold_btc_nor_best = RandomForestRegressor(n_estimators=200, max_depth=3, max_features=4, random_state=42)
rfr_gold_btc_nor_best.fit(train_features, train_targets)

train_predictions = rfr_gold_btc_nor_best.predict(train_features)
test_predictions = rfr_gold_btc_nor_best.predict(test_features)

plt.scatter(train_targets, train_predictions, label='train')
plt.scatter(test_targets, test_predictions, label='test')
plt.legend()
plt.show()
# —————————————————————————————————————————————————————— random forest ——————————————————————————————————————————————————————————————————————————————————————————————————







# —————————————————————————————————————————————————————— GradientBoostingRegressor ——————————————————————————————————————————————————————————————————————————————————————————————————
# gbr = GradientBoostingRegressor(max_features=4,
#                                 learning_rate=0.01,
#                                 n_estimators=200,
#                                 subsample=0.6,
#                                 random_state=42)
# gbr.fit(train_features, train_targets)
#
# print(gbr.score(train_features, train_targets))
# print(gbr.score(test_features, test_targets))
# —————————————————————————————————————————————————————— GradientBoostingRegressor ——————————————————————————————————————————————————————————————————————————————————————————————————
