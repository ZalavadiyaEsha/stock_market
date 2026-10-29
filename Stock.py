import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "Date": [
        "2026-10-01",
        "2026-10-02",
        "2026-10-03",
        "2026-10-04",
        "2026-10-05",
        "2026-10-06",
        "2026-10-07",
        "2026-10-08",
        "2026-10-09",
        "2026-10-10"
    ],
    "Close": [100, 105, 103, 110, 115, 112, 120, 118, 125, 130],
    "Volume": [1000, 1200, 1100, 1500, 1800, 1400, 2000, 1700, 2200, 2500]
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
print("Stock Market Data:")
print(df)
df["Moving_Average"] = df["Close"].rolling(window=5).mean()
average_price = np.mean(df["Close"])
highest_price = np.max(df["Close"])
lowest_price = np.min(df["Close"])
print("\nStock Market Analysis")
print("Average Price:", round(average_price, 2))
print("Highest Price:", highest_price)
print("Lowest Price:", lowest_price)
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Close"], marker="o", label="Stock Price")
plt.plot(df["Date"], df["Moving_Average"], label="5-Day Moving Average")
plt.title("Stock Market Analysis")
plt.xlabel("Date")
plt.ylabel("Stock Price (Rs.)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 5))
plt.bar(df["Date"], df["Volume"])
plt.title("Stock Trading Volume")
plt.xlabel("Date")
plt.ylabel("Trading Volume")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()
print("\nStock Market Analysis Completed Successfully!")