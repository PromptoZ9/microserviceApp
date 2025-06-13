from .bp import btc_getter
from app import mail
from flask_mail import Message
import requests
from flask import request
from datetime import datetime
import os

@btc_getter.route("/")
def index():
    return "do /btc_getter/get_btc in thunder client to get btc price"


@btc_getter.route("/get_btc", methods=["POST"])
def get_btc():
    email = request.form.get("EMAIL")
    url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&include_last_updated_at=true"
    headers = {"accept": "application/json",
               "x-cg-demo-api-key": os.getenv("COINGECKO_API_KEY"),
    }
    request.get_data()
    resp = requests.get(url, headers = headers)
    jsonData= resp.json()
    last_updated_at = datetime.fromtimestamp(jsonData['bitcoin']['last_updated_at'])
    data = {
        "statusCode" : 200, 
        'coin' : 'btc', 
        'usd' : jsonData['bitcoin']['usd'], 
        'last_updated_at' : last_updated_at,
        }
    if email:
        message = Message(
            f"BTC Information - {datetime.now().strftime('%Y-%m-%d')}", 
            recipients=[email],
            body = f"""
Hello, {email}

Today's 1 BTC price is at {data['usd']} 
source: https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&include_last_updated_at=true
            
            """,
        )
        mail.send(message)
    return data






