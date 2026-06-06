import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1
}

response = requests.get(url, params=params)

data = response.json()

df = pd.DataFrame(data)

df = df[
    [
        'name',
        'symbol',
        'current_price',
        'market_cap',
        'total_volume',
        'price_change_percentage_24h'
    ]
]

print(df.head())

df.to_csv("data/crypto_data.csv", index=False)

print("CSV file saved successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())



import matplotlib.pyplot as plt

top10 = df.sort_values(
    by="market_cap",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))

plt.bar(
    top10['name'],
    top10['market_cap']
)

plt.title("Top 10 Cryptocurrencies by Market Cap")
plt.xlabel("Cryptocurrency")
plt.ylabel("Market Cap")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

top_gainer = df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
).head(1)

print("\nTop Gainer in Last 24 Hours:")
print(top_gainer)

highest_volume = df.sort_values(
    by="total_volume",
    ascending=False
).head(1)

print("\nHighest Trading Volume:")
print(highest_volume)

# Highest Market Cap
highest_market_cap = df.sort_values(
    by="market_cap",
    ascending=False
).head(1)

print("\nHighest Market Cap:")
print(highest_market_cap)

# Top Gainer
top_gainer = df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
).head(1)

print("\nTop Gainer (24 Hours):")
print(top_gainer)

# Biggest Loser
biggest_loser = df.sort_values(
    by="price_change_percentage_24h",
    ascending=True
).head(1)

print("\nBiggest Loser (24 Hours):")
print(biggest_loser)

# Highest Trading Volume
highest_volume = df.sort_values(
    by="total_volume",
    ascending=False
).head(1)

print("\nHighest Trading Volume:")
print(highest_volume)

# Top 10 Coins by Trading Volume

top10_volume = df.sort_values(
    by="total_volume",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))

plt.bar(
    top10_volume['name'],
    top10_volume['total_volume']
)

plt.title("Top 10 Cryptocurrencies by Trading Volume")
plt.xlabel("Cryptocurrency")
plt.ylabel("Trading Volume")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()