from textblob import TextBlob


testimonial = TextBlob("I love you")
print(testimonial.sentiment, testimonial.sentiment.polarity)

if testimonial.sentiment.polarity > 0:
    print("positive")
elif testimonial.sentiment.polarity < 0:
    print("negative")
else:
    print("neutral")