# open the file
file = open("/workspaces/DATA3500_griffith_gotchy/TSLA.csv")

lines = file.readlines()[1:]  # skip header

# list to store closing prices
prices = []

# tracking variables
buy = None
first_buy = None
total_profit = 0
trade_number = 0

for line in lines:
    # clean and extract closing price
    parts = line.strip().split(",")
    price_str = parts[4].replace("$", "")  # assuming 5th column is Close
    current_price = float(price_str)
    prices.append(current_price)

    # only calculate once we have 5 prices
    if len(prices) >= 5:
        moving_avg = sum(prices[-5:]) / 5

        # buy condition
        if current_price < moving_avg * 0.98 and buy is None:
            buy = current_price
            if first_buy is None:
                first_buy = buy
            print(f"Buy at ${buy:.2f}")

        # sell condition
        elif current_price > moving_avg * 1.02 and buy is not None:
            sell = current_price
            profit = sell - buy
            total_profit += profit
            trade_number += 1
            print(f"Trade {trade_number}: Sell at ${sell:.2f}, Profit = ${profit:.2f}")
            buy = None  # reset after selling

# calculate final profit percentage
if first_buy is not None and first_buy != 0:
    final_profit_percentage = (total_profit / first_buy) * 100
    print(f"\nTotal Profit from all trades: ${total_profit:.2f}")
    print(f"Final Profit Percentage: {final_profit_percentage:.2f}%")
else:
    print("No trades executed.")

file.close()
