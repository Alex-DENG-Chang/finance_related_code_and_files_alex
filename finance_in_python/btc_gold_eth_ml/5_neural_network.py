import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
import seaborn as sns
import statsmodels.api as sm
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score
import keras.losses
import tensorflow as tf
from keras.layers import Input

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


features = pd.DataFrame({
     'Gold Close': gold_close_nor_df,
     'VIX Close': vix_close_nor_df,
     'ETH CLOSE': eth_close_nor_df
 })

targets = btc_close_nor_df

linear_features = sm.add_constant(features)
train_size = int(0.85 * targets.shape[0])
train_features = linear_features[:train_size]
train_targets = targets[:train_size]
test_features = linear_features[train_size:]
test_targets = targets[train_size:]
# —————————————————————————————————————————————————————— data prepare ——————————————————————————————————————————————————————————————————————————————————————————————————






print(train_features.shape)
# —————————————————————————————————————————————————————— neural net (2L)——————————————————————————————————————————————————————————————————————————————————————————————————
# Create the model
model_1 = Sequential()
model_1.add(Dense(128, input_dim=train_features.shape[1], activation='relu'))
model_1.add(Dense(64, activation='relu'))
model_1.add(Dense(1, activation='linear'))

# Fit the model
model_1.compile(optimizer='adam', loss='mse')
history = model_1.fit(train_features, train_targets, epochs=25)

# Plot the losses from the fit
plt.plot(history.history['loss'])

# Use the last loss as the title
plt.title('loss:' + str(round(history.history['loss'][-1], 6)))
plt.show()

# Calculate R^2 score
train_preds = model_1.predict(train_features)
test_preds = model_1.predict(test_features)
print('R^2 of train data: ', r2_score(train_targets, train_preds))
print('R^2 of test data: ', r2_score(test_targets, test_preds))

# Plot predictions vs actual
plt.scatter(train_preds, train_targets, label='train')
plt.scatter(test_preds, test_targets, label='test')
plt.legend()
plt.show()
# —————————————————————————————————————————————————————— neural net ——————————————————————————————————————————————————————————————————————————————————————————————————




# —————————————————————————————————————————————————————— neural net with pen ——————————————————————————————————————————————————————————————————————————————————————————————————
# def sign_penalty(y_true, y_pred):
#     penalty = 100.
#     loss = tf.where(tf.less(y_true * y_pred, 0), \
#                      penalty * tf.square(y_true - y_pred), \
#                      tf.square(y_true - y_pred))
#
#     return tf.reduce_mean(loss, axis=-1)
#
# keras.losses.sign_penalty = sign_penalty  # enable use of loss with keras
#
# # Create the model
# model_2 = Sequential()
# model_2.add(Dense(100, input_dim=train_features.shape[1], activation='relu'))
# model_2.add(Dense(20, activation='relu'))
# model_2.add(Dense(1, activation='linear'))
#
# # Fit the model
# model_2.compile(optimizer='adam', loss='sign_penalty')
# history = model_2.fit(train_features, train_targets, epochs=25)
#
# # Plot the losses from the fit
# plt.plot(history.history['loss'])
#
# # Use the last loss as the title
# plt.title('loss:' + str(round(history.history['loss'][-1], 6)))
# plt.show()
#
# # Calculate R^2 score
# train_preds = model_2.predict(train_features)
# test_preds = model_2.predict(test_features)
# print(r2_score(train_targets, train_preds))
# print(r2_score(test_targets, test_preds))
#
# # Plot predictions vs actual
# plt.scatter(train_preds, train_targets, label='train')
# plt.scatter(test_preds, test_targets, label='test')
# plt.legend()
# plt.show()
# —————————————————————————————————————————————————————— neural net with pen ——————————————————————————————————————————————————————————————————————————————————————————————————









# —————————————————————————————————————————————————————— neural net (3L)——————————————————————————————————————————————————————————————————————————————————————————————————
# Create the model
# model_1 = Sequential()
# model_1.add(Dense(100, input_dim=train_features.shape[1], activation='relu'))
# model_1.add(Dense(20, activation='relu'))
# model_1.add(Dense(20, activation='relu'))
# model_1.add(Dense(1, activation='linear'))
#
# # Fit the model
# model_1.compile(optimizer='adam', loss='mse')
# history = model_1.fit(train_features, train_targets, epochs=25)
#
# # Plot the losses from the fit
# plt.plot(history.history['loss'])
#
# # Use the last loss as the title
# plt.title('loss:' + str(round(history.history['loss'][-1], 6)))
# plt.show()
#
# # Calculate R^2 score
# train_preds = model_1.predict(train_features)
# test_preds = model_1.predict(test_features)
# print('R^2 of train data: ', r2_score(train_targets, train_preds))
# print('R^2 of test data: ', r2_score(test_targets, test_preds))
#
# # Plot predictions vs actual
# plt.scatter(train_preds, train_targets, label='train')
# plt.scatter(test_preds, test_targets, label='test')
# plt.legend()
# plt.show()
# —————————————————————————————————————————————————————— neural net (3L)——————————————————————————————————————————————————————————————————————————————————————————————————