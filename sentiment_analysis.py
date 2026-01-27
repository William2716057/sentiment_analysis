from textblob import TextBlob
import json
from pathlib import Path
#change to pdf read 
#extract text segments for formatting
#options to search for specific data (names, keywords)
def analyze_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError("File is empty")

    blob = TextBlob(text)
    
    #sentiment
    sentiment = blob.sentiment
    
    #display word count
    #sentence count
    #average sentence length
    #lexical diversity
    #punctuation density

    #counts
    #words
    words = blob.words
    word_count = len(words)
    #sentences
    sentences = blob.sentences
    sentence_count = len(sentences)
    
    #lexical diversity
    unique_words = set(word.lower() for word in words)
    lexical_diversity = (
        len(unique_words) / word_count if word_count > 0 else 0
        )
    
    avg_sentence_length = (
        word_count / sentence_count if sentence_count > 0 else 0
    )

    return {
        "word count": word_count,
        "average sentence length": round(avg_sentence_length, 2),
        "lexical diversity": round(lexical_diversity, 4),
        
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity,
        "label": label(sentiment.polarity),
    }
    #return

def label(polarity):
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    return "neutral"

def main():
    file_path = Path(input("Enter file: ").strip())
    
    if not file_path.exists():
        print("File not found.")
        return
    try:
        results = analyze_file(file_path)
        print(json.dumps(results, indent=2))
    except Exception as e:
        print(f"error: {e}")
        

if __name__ == "__main__":
    main()