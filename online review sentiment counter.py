reviews = [
    {"review_id": 1, "sentiment": "positive"},
    {"review_id": 2, "sentiment": "negative"},
    {"review_id": 3, "sentiment": "positive"},
    {"review_id": 4, "sentiment": "neutral"},
    {"review_id": 5, "sentiment": "positive"}
]
sentiment_count = {}
for review in reviews:
    s = review["sentiment"]
    sentiment_count[s] = sentiment_count.get(s, 0) + 1
top_sentiment = max(sentiment_count, key=sentiment_count.get)
print("Sentiment count:")
print(sentiment_count)
print("\nSentiment with maximum occurrence:")
print(top_sentiment)
