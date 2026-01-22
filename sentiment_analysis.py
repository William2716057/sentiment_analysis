import string
from textblob import TextBlob
import json

#text = input("Enter text: ")
file_path = input("Enter file: ")

with open(file_path, 'r') as file:
    text = file.read()
    blob = TextBlob(text)
    
sentiment = blob.sentiment
    
results = {
    "polarity": sentiment.polarity,
    "subjectivity": sentiment.subjectivity}

print(json.dumps(blob.sentiment))

