from gensim.models import KeyedVectors
from flask import current_app
from transformers import AutoTokenizer, AutoModel
from .embeddings import find_meanings, similarity, fasttext
from .bert import labse, tiny_bert

model = None
tokenizer = None


def pipeline(text: str, word: str, extractor) -> (str, float):

    text_emb = extractor(text, model, tokenizer)
    m, e = find_meanings(word)

    mx_m = ""
    mx_score = 0
    for i in range(len(m)):
        if m[i]:
            if e[i]:
                m_emb = extractor(m[i] + "." + e[i], model,  tokenizer)
            else:
                m_emb = extractor(m[i], model)
            score = similarity(m_emb, text_emb)
            if score > mx_score:
                mx_score = score
                mx_m = m[i]

    return mx_m, mx_score


def load_vectors():
    global model, tokenizer

    conf = current_app.config["MODEL"]
    if conf == "fasttext":
        model = KeyedVectors.load(current_app.config["FASTTEXT"])
    elif conf == "tinybert":
        tokenizer = AutoTokenizer.from_pretrained(current_app.config["TINYBERT"])
        model = AutoModel.from_pretrained(current_app.config["TINYBERT"])
    elif conf == "labse":
        tokenizer = AutoTokenizer.from_pretrained(current_app.config["LABSE"])
        model = AutoModel.from_pretrained(current_app.config["LABSE"])


def main(text, word):
    conf = current_app.config["MODEL"]

    if conf == "fasttext":
        return pipeline(text, word, extractor=fasttext)
    elif conf == "tinybert":
        return pipeline(text, word, extractor=tiny_bert)
    elif conf == "labse":
        return pipeline(text, word, extractor=labse)
    else:
        return "error", 0
