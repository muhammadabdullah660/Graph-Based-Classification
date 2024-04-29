#from scrapping import scrape_and_save_data
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string
import os

# Download NLTK resources (run once)
# nltk.download('punkt')
# nltk.download('stopwords')

# Initialize stemmer and stopwords
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))


def preprocess_text(raw_text):
    # Tokenization
    tokens = word_tokenize(raw_text.lower())
    # Removing punctuations and stopwords, and stemming
    processed_tokens = []
    for token in tokens:
        if token not in string.punctuation and token not in stop_words:
            processed_token = stemmer.stem(token)
            processed_tokens.append(processed_token)

    # Remove duplicate words
    unique_tokens = list(set(processed_tokens))

    return unique_tokens


def preprocess_files(folder):
    for file_name in os.listdir(folder):
        if file_name.endswith('.txt'):
            with open(os.path.join(folder, file_name), 'r', encoding='utf-8') as file:
                raw_text = file.read()
                preprocessed_text = preprocess_text(raw_text)
                with open(os.path.join(folder, f"preprocessed_{file_name}"), 'w', encoding='utf-8') as preprocessed_file:
                    preprocessed_file.write(' '.join(preprocessed_text))


# Preprocess files
preprocess_files('.')  # Specify the folder where the scraped files are stored

print("Data scraped, preprocessed, and saved successfully.")
