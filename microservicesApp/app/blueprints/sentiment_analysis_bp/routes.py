from .bp import sentiment_analysis_bp as sa_bp
from textblob import TextBlob
from flask import request


@sa_bp.route("/")
def index():
    return "do /sentiment_analysis/do_analysis in thunder client to do sentiment analysis"

@sa_bp.route("/do_analysis", methods=["POST"])
def do_analysis():
    text = request.form.get("text")
    testimonial = TextBlob(text)
    if testimonial.sentiment.polarity > 0:
        return {"sentiment": "positive"}
    elif testimonial.sentiment.polarity < 0:
        return {"sentiment": "negative"}
    else:
        return {"sentiment": "neutral"}