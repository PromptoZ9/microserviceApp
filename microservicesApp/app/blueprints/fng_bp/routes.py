from .bp import fng_bp
from app import mail
from flask_mail import Message

import requests
from datetime import datetime
from dataclasses import dataclass

@dataclass
class FearAndGreedIndex:
    value: int
    classification: str

@fng_bp.route("/")
def index():
    return "do /fng/get_fng/<email> to get fng index"

@fng_bp.route("/get_fng/<email>")
def get_fng(email):
    resp = requests.get("https://api.alternative.me/fng/").json()
    fng = FearAndGreedIndex(
    value = resp['data'][0]['value'], 
    classification=resp['data'][0]['value_classification']
)
    date = datetime.now().strftime("%Y-%m-%d")
    message = Message(subject=f"Fear and Greed - date {date} - {fng.classification}", 
                      recipients=[email], 
                      body=f"Today's Fear and Greed {date} is at value {fng.value} with classification {fng.classification} \n\n source: https://api.alternative.me/fng/")
    
    mail.send(message)
    return 200



