import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *

import re
from bs4 import BeautifulSoup

nltk.download('stopwords')
nltk.download('words')

def lyrics_to_words(lyrics):
    '''
    helper function to clean out song lyrics. We apply porter Stemmer algorithm and remove stopwords
    '''
    stopwords = nltk.corpus.stopwords.words('english')
    newStopWords = ['verse','1', '2', 'chorus', 'bridge', 'talking', 'refrain', 'explain', 'request']
    stopwords.extend(newStopWords)
    stemmer = PorterStemmer()
    
    words_english = set(nltk.corpus.words.words())

    remove_non_english = " ".join(w for w in nltk.wordpunct_tokenize(lyrics) if w.lower() in words_english or not w.isalpha())
    
    text = re.sub(r"[^a-zA-Z0-9]", " ", remove_non_english.lower()) # Convert to lower case
    words = text.split() # Split string into words
    words = [w for w in words if w not in stopwords] # Remove stopwords
    words = [PorterStemmer().stem(w) for w in words] # stem
    
    return words


def convert_and_pad(word_dict, sentence, pad=500):
    NOWORD = 0 # We will use 0 to represent the 'no word' category
    INFREQ = 1 # and we use 1 to represent the infrequent words, i.e., words not appearing in word_dict
    
    working_sentence = [NOWORD] * pad
    
    for word_index, word in enumerate(sentence[:pad]):
        if word in word_dict:
            working_sentence[word_index] = word_dict[word]
        else:
            working_sentence[word_index] = INFREQ
            
    return working_sentence, min(len(sentence), pad)