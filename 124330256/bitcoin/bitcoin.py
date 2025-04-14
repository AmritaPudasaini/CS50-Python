import requests
import sys
import json

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)
else:
    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o=response.json()
        price_per_bitcoin = o["bpi"]["USD"]["rate_float"]
        total_cost = float(bitcoin * price_per_bitcoin)
        total_cost_bitcoin = "{:,.4f}".format(total_cost)
        print(f"${total_cost_bitcoin}")
    except requests.RequestException:
        sys.exit(1)
