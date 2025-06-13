import requests
from datetime import datetime
from dataclasses import dataclass


@dataclass
class NewsApiArticle:
    source : str
    author : str
    title : str
    description : str
    url : str
    urlToImage : str
    publishedAt : datetime
    content : str
    def __post_init__(self):
        self.publishedAt = datetime.strptime(self.publishedAt, "%Y-%m-%dT%H:%M:%SZ")
        self.source= self.source["id"]
        
url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=6b4cac847b6f45d1852e413c2a2458fb"     
resp = requests.get(url).json()

output = []
for news in resp ['articles']:
    news = NewsApiArticle(**news)
    output.append(news)
    
print(output[0])

    