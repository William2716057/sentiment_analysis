import string
from textblob import TextBlob


text = input("Enter text: ")
blob = TextBlob(text)

print(blob.sentiment)


# Dictionary of positive words
POSITIVE_WORDS = {
    "good", "great", "excellent", "awesome", "happy",
    "love", "like", "fantastic", "amazing", "nice",
    "positive", "enjoy", "pleased"
}
#dictionary of negative words
NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "hate", "angry",
    "sad", "horrible", "poor", "negative", "worse",
    "worst", "disappointed"
}

def analyze_sentiment(text):
    # Normalize text
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()

    score = 0

    for word in words:
        if word in POSITIVE_WORDS:
            score += 1
        elif word in NEGATIVE_WORDS:
            score -= 1

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "score": score,
        "sentiment": sentiment
    }

#change to text file
#if __name__ == "__main__":
#    text = input("Enter text: ")
#    result = analyze_sentiment(text)
#    print(result)
