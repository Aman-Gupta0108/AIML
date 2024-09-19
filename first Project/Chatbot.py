def sentiment_analysis(text):
    # List of positive and negative words
    positive_words = ["good", "happy", "love", "excellent", "great","joyful","grateful","radiant","inspiring","vibrant","optimistic","hopeful","brilliant","confident","harmonious","enthusiastic","courageous","compassionate","empowered","resilient","uplifting","creative","peaceful","blessed","successful",]
                     
    negative_words = ["bad", "sad", "hate", "terrible", "poor","not","never","neither","barely","hardly","scarcely","seldom","rarely","nothing","none","no one","nobody","nowhere"]

    # Convert the text to lowercase and split into words
    words = text.lower().split()
    
    # Count the number of positive and negative words
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    
    # Determine sentiment based on counts
    if pos_count > neg_count:
        return "Positive"
    elif pos_count < neg_count:
        return "Negative"
    else:
        return "Neutral"

text = input("Enter a sentence: ")
print("Sentiment:", sentiment_analysis(text))

