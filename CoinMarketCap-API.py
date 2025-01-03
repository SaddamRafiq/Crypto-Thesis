import requests

# Your CoinMarketCap API key
api_key = '3d2992f7-bbca-46bf-a1ef-00caf37c0390'

# Endpoint for latest cryptocurrency data
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Parameters for the API request
parameters = {
    'start': '1',
    'limit': '5000',  # Limit the results to the top 10 cryptocurrencies
    'convert': 'USD'
}

# Headers with the API key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

# Send the request
response = requests.get(url, headers=headers, params=parameters)
data = response.json()

# Print the cryptocurrency data
for crypto in data['data']:
    print(f"Name: {crypto['name']}, Price: {crypto['quote']['USD']['price']}")
