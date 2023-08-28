import re
import nltk
import string
import requests
import numpy as np
from bs4 import BeautifulSoup
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity


# (text, word) --> meaning text

def tokenize(text):
    russian_stopwords = set(nltk.corpus.stopwords.words('russian'))

    punctuation = re.compile(r"[" + string.punctuation + string.ascii_letters + string.digits + "]")

    words = nltk.word_tokenize(text)

    words = [word for word in words if word not in russian_stopwords]

    return [word for
            word in words
            if not re.search(punctuation, word)]


def load_vectors():
    return KeyedVectors.load('/app/backend/core/model/fasttext/model.model')


def vectorize_sentence(text):
    tokens = tokenize(text)
    model = load_vectors()

    def use_model(x):
        return model[str(x)]

    text_array = np.array(list(map(use_model, tokens)))
    res = text_array.sum(axis=0)
    return res


def find_meanings(word):
    url = f"https://ru.wiktionary.org/wiki/{word}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    meanings = []
    examples = []

    content = soup.find('ol')
    if content:
        for li in content.find_all('li'):
                row = li.text
                index = row.find("◆")
                if index:
                    meanings.append(row[:index])
                    examples.append(row[index+1:])
                else:
                    meanings.append(row)
                    examples.append([])

    return meanings, examples


def similarity(vec1, vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)

    return cosine_similarity(vec1, vec2)[0][0]


def main(text, word):

    text_emb = vectorize_sentence(text)
    m, e = find_meanings(word)

    mx_m = ""
    mx_score = 0
    for i in range(len(m)):
        if m[i]:
            if e[i]:
                m_emb = vectorize_sentence(m[i] + "." + e[i])
            else:
                m_emb = vectorize_sentence(m[i])
            score = similarity(m_emb, text_emb)
            if score > mx_score:
                mx_score = score
                mx_m = m[i]

    return mx_m, mx_score
