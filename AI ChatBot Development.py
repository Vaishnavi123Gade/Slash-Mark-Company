import numpy as np
import nltk
import string
import random

f=open("chatbot.txt","r",errors="ignore")
raw_doc=f.read()
raw_doc=raw_doc.lower()
nltk.download("punkt")
nltk.download("wordnet")
sent_tokens=nltk.sent_tokenize(raw_doc)
word_tokens=nltk.word_tokenize(raw_doc)

sent_tokens[:2:]
word_tokens[:2:]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return[lemmer.lemmatize(token) for token in tokens]
remove_punkt_dict = dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREET_INPUTS=("hello","hii","greetings","what's up","heyy")
GREET_RESPONSES=["Hii","Hey","hii there","I am glad !!! You are talking to me"]
def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise  import cosine_similarity

def response(user_response):
    robol_response=''
    TfidfVec=TfidfVectorizer(tokenizer=LemNormalize,stop_words='english')
    tfidf=TfidfVec.fit_transform(sent_tokens)
    vals=cosine_similarity(tfidf[-1],tfidf)
    idx=vals.argsort()[0][-2]
    flat=vals.flatten()






