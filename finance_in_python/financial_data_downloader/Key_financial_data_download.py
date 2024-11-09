import yfinance as yf

ateyy = yf.Ticker("ATEYY")


print(ateyy.analyst_price_targets)
print(ateyy.earnings_estimate)
print(ateyy.revenue_estimate)
print(ateyy.earnings_history)
print(ateyy.eps_trend)
print(ateyy.eps_revisions)
print(ateyy.growth_estimates)