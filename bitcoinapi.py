import requests
import json

#    Get BTC price
res = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
data = res.json()
btc_name = data[0]['symbol'] 
btc_price = float(data[0]['price_usd'])
print("1 " + btc_name + " = ", btc_price)


#    Get THB price
url = 'https://api.exchangeratesapi.io/latest?base=' + 'USD'
response = requests.get(url)
data_currency = response.text
parsed = json.loads(data_currency)
rates = parsed["rates"]


#    Calculate to THB
thb_price = rates['THB']
calculate_price = btc_price * thb_price
print("1 USD = {}".format(thb_price))
print("Summary: 1 BTC = {:,.2f} baht".format(calculate_price))


