import string
# Function to count number of words
def count_words(text):
    # Remove punctuation marks
    translator = str.maketrans('', '', string.punctuation)
    text_cleaned = text.translate(translator)
    
    # Split text into words
    words = text_cleaned.split()
    
    # Count the number of words
    return len(words)
