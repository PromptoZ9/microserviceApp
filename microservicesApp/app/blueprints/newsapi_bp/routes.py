from .bp import newsapi_bp
from flask import request
import requests
import os
from .models import NewsApiArticle
from app import mail
from flask_mail import Message
from datetime import datetime
from .models import NewsApiArticle


@newsapi_bp.route("/get_news", methods = ["POST"])
def get_news():
    email = request.form.get("email")
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={os.getenv('NEWS_API_KEY')}"     
    resp = requests.get(url).json()
    
    output = []
    for news in resp ['articles']:
        news = NewsApiArticle(**news)
        if news.url == "https://removed.com":
            continue
        output.append(news)
    newsStringOutput = ''
    for n in output:
        newsStringOutput = newsStringOutput + f"{n.title} - {n.source} \n {n.description} \n Url: {n.url} \n\n"
    message = Message(f"Top technews for today - {datetime.now().strftime('%Y-%m-%d')}", 
                      recipients= [email if email is not None else os.getenv("EMAIL")],
                      body = f"""
dear recipients,

here are today's top technews:

""" + newsStringOutput,
    )
    mail.send(message)
    return {"status_code" : 200}






 