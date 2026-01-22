import string
from textblob import TextBlob
import json

#enter user file 
file_path = input("Enter file: ")

#open file
with open(file_path, 'r') as file:
    text = file.read()
    blob = TextBlob(text)
    
sentiment = blob.sentiment

def label(polarity):
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    return "neutral"

#create results json output    
results = {
    "polarity": sentiment.polarity,
    "subjectivity": sentiment.subjectivity,
    "Label": label(sentiment.polarity)
    }

#print in json format
print(json.dumps(results, indent=2))



