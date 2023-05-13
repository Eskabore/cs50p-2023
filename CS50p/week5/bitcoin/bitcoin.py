import sys
import requests

# Check if user has provided a command-line argument
if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py <address>")

# Try to convert the command-line argument to a float:
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Usage: python bitcoin.py <address>")

# Query the API for current price of Bitcoin
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price = data['bpi']['USD']['rate_float']
except requests.RequestException:
    sys.exit("Error: API request failed")

# Compute the value of the user's Bitcoin in USD
amount = n * price
print(f"{n} BTC is worth ${amount:,.4f}")
