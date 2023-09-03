import re
import string
import nltk
import requests
import numpy as np
from bs4 import BeautifulSoup
from sklearn.metrics.pairwise import cosine_similarity


def tokenize(text):
    russian_stopwords = set(nltk.corpus.stopwords.words('russian'))

    punctuation = re.compile(r"[" + string.punctuation + string.ascii_letters + string.digits + "]")

    words = nltk.word_tokenize(text)

    words = [word for word in words if word not in russian_stopwords]

    return [word for
            word in words
            if not re.search(punctuation, word)]


def fasttext(text, model, *args):
    tokens = tokenize(text)

    def use_model(model_input):
        return model[str(model_input)]

    text_array = np.array(list(map(use_model, tokens)))
    res = text_array.mean(axis=0)
    return res


def find_meanings(word):
    url = f"https://ru.wiktionary.org/wiki/{word}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    meanings = []
    examples = []

    content = soup.find('ol')
    if content:
        for elements in content.find_all('li'):
            row = elements.text
            index = row.find("◆")
            if index:
                meanings.append(row[:index])
                if row[index+2:][:11] == "Отсутствует":
                    examples.append('')
                else:
                    examples.append(row[index+2:])
            else:
                meanings.append(row)
                examples.append('')

    return meanings, examples


def similarity(vec1, vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)

    return cosine_similarity(vec1, vec2)[0][0]
