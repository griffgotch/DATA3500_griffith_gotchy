import json

import json

# ---------------------------------------------
# MEAN REVERSION STRATEGY
# ---------------------------------------------
def meanReversionStrategy(prices):
    cash = 0
    shares = 0

    for i in range(5, len(prices)):
        window = prices[i-5:i]
        avg = sum(window) / 5
        price = prices[i]

        # BUY signal
        if price < avg * 0.98:
            print("Mean Reversion BUY at:", price)
            shares += 1
            cash -= price

        # SELL signal
        elif price > avg * 1.02:
            print("Mean Reversion SELL at:", price)
            shares -= 1
            cash += price

    # Final value: convert remaining shares to cash
    final_value = cash + shares * prices[-1]
    profit = final_value
    return_percentage = (final_value / prices[0] - 1) * 100

    return round(profit, 2), round(return_percentage, 2)


# ---------------------------------------------
# SIMPLE MOVING AVERAGE STRATEGY
# ---------------------------------------------
def simpleMovingAverageStrategy(prices):
    cash = 0
    shares = 0

    for i in range(5, len(prices)):
        window = prices[i-5:i]
        avg = sum(window) / 5
        price = prices[i]

        # BUY signal
        if price > avg:
            print("SMA BUY at:", price)
            shares += 1
            cash -= price

        # SELL signal
        elif price < avg:
            print("SMA SELL at:", price)
            shares -= 1
            cash += price

    final_value = cash + shares * prices[-1]
    profit = final_value
    return_percentage = (final_value / prices[0] - 1) * 100

    print("final value:", final_value)
    print("profit", profit)
    print("return precentage", return_percentage)


    return round(profit, 2), round(return_percentage, 2)


# ---------------------------------------------
# SAVE RESULTS TO JSON
# ---------------------------------------------
def saveResults(results):
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)
    print("\nResults saved to results.json")


# ---------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------

tickers = [
    "AAPL", "GOOG", "ADBE",
    "TSLA", "BA", "CMCSA", "CSCO", "CVX", "JPM", "V"
]

results = {}

for ticker in tickers:
    print("\n----------------------------------")
    print("Processing:", ticker)
    print("----------------------------------")

    # Load the prices
    
    filename = f"/workspaces/DATA3500_griffith_gotchy/TSLA.csv"
    prices = []

with open(filename) as file:
    lines = file.readlines()[1:]  # skip header line

    for line in lines:
        parts = line.strip().split(",")        # split CSV line
        price_str = parts[1].replace("$", "")  # remove the $ sign
        prices.append(round(float(price_str), 2))

    # Store prices
    results[f"{ticker}_prices"] = prices

    # Run Mean Reversion
    mr_profit, mr_returns = meanReversionStrategy(prices)
    results[f"{ticker}_mr_profit"] = mr_profit
    results[f"{ticker}_mr_returns"] = mr_returns

    # Run Simple Moving Average
    sma_profit, sma_returns = simpleMovingAverageStrategy(prices)
    results[f"{ticker}_sma_profit"] = sma_profit
    results[f"{ticker}_sma_returns"] = sma_returns


# Save all results
saveResults(results)
