prices = [100, 102, 101, 103, 106, 105, 108, 110, 109, 112]
last_three_prices = prices[-3:]
moving_average = sum(last_three_prices) / len(last_three_prices)

latest_price = prices[-1]

if latest_price > moving_average:
    print("BUY")
elif latest_price < moving_average:
    print("SELL")
else:
    print("HOLD")