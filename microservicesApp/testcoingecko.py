import requests, os
from datetime import datetime

def getBitcoinPrice():
    
    url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&include_last_updated_at=true"
    API_KEY = os.getenv("COINGECKO_API_KEY")
    headers = {"accept": "application/json",
               "x-cg-demo-api-key": API_KEY,
    }
    
    resp = requests.get(url, headers = headers)
    jsonData= resp.json()
    last_updated_at = datetime.fromtimestamp(jsonData['bitcoin']['last_updated_at'])
    return {
        "statusCode" : 200, 
        'coin' : 'btc', 
        'usd' : jsonData['bitcoin']['usd'], 
        'last_updated_at' : last_updated_at,
        }

x = getBitcoinPrice()
print(x)
