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

#create results json output    
results = {
    "polarity": sentiment.polarity,
    "subjectivity": sentiment.subjectivity
    }

#print in json format
print(json.dumps(results, indent=2))



