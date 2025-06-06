import re
import string
import nltk
import contractions
import emoji
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import spacy


nltk.download('averaged_perceptron_tagger', download_dir='./nltk_data')
nltk.download('punkt', download_dir='./nltk_data')
nltk.download('punkt_tab', download_dir='./nltk_data')
nltk.download('stopwords', download_dir='./nltk_data')
nltk.download('wordnet', download_dir='./nltk_data')
nltk.data.path.append('./nltk_data')

# python -m spacy download en
# python -m spacy download en_core_web_md
nlp = spacy.load("en_core_web_sm")

# logger = setup_logger()

def expand_contractions(text):
    '''
    Expands contractions in text to full form.

    Example: 
    >>> expand_contractions("I can't do this")
        "I cannot do this"
    '''
    return contractions.fix(text)

def replace_emoji(text):
    '''
    Replace Emoji in text with corresponding text description
    '''
    return emoji.demojize(text).replace("_", " ").replace(":", " ")

def lowercase_text(text):
    '''
    Convert text to lowercase.
    '''
    return text.lower()

def remove_punctuation(text):
    '''
    Remove punctuation from text.
    '''
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_numbers(text):
    '''
    Remove numbers from text.
    '''
    return re.sub(r'\d+', '', text)

def remove_special_characters(text):
    '''
    Remove special characters from text
    '''
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def remove_whitespace(text):
    '''
    Remove extra whitespaces from text
    '''
    return text.strip()

def remove_stopwords(text):
    '''
    Remove stopwords from text
    '''
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    return ' '.join([word for word in tokens if word not in stop_words])

"""
def get_wordnet_pos(word):
    '''Map POS tag to first character lemmatize() accepts'''
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

def lemmatize_text(text):
    '''
    Lemmatize text considering the part-of-speech of each word.
    '''
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    lemmatized_output = ' '.join([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in tokens])
    return lemmatized_output
"""

def lemmatize_text_spacy(text):
    '''
    Lemmatize text using spaCy, considering the part-of-speech and context of each word.
    '''
    doc = nlp(text)    
    lemmatized_output = ' '.join([token.lemma_ for token in doc])

    return lemmatized_output

def clean_text(text):
    '''
    Apply all cleaning functions to text
    '''
    # print(f'expand_contractions: {text}')
    text = expand_contractions(text)
    # print(f'replace_emoji: {text}')
    text = replace_emoji(text)
    # print(f'lowercase_text: {text}')
    text = lowercase_text(text)
    # print(f'remove_special_characters: {text}')
    text = remove_special_characters(text)
    # print(f'remove_punctuation: {text}')
    text = remove_punctuation(text)
    # print(f'remove_numbers: {text}')
    text = remove_numbers(text)
    # print(f'remove_whitespace: {text}')
    text = remove_whitespace(text)
    # print(f'remove_stopwords: {text}')
    text = remove_stopwords(text)
    # print(f'lemmatize_text: {text}')
    lemmatized_output = lemmatize_text_spacy(text)
    # print(f'Done, Returning lemmatized_output: {lemmatized_output}')
    return lemmatized_output