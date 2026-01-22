import string
from textblob import TextBlob


text = input("Enter text: ")
blob = TextBlob(text)

print(blob.sentiment)

