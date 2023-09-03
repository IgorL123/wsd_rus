from multiprocessing import Pool
from gensim.models import KeyedVectors
from flask import current_app
from transformers import AutoTokenizer, AutoModel
from .embeddings import find_meanings, similarity, fasttext
from .bert import labse, tiny_bert


MODEL = None
TOKENIZER = None


def pipeline(text: str, word: str, extractor) -> (str, float):

    text_emb = extractor(text, MODEL, TOKENIZER)
    (meaning, embed) = find_meanings(word)

    mx_m = ""
    mx_score = 0
    for ind, mean in enumerate(meaning):
        if mean:
            if embed[ind]:
                m_emb = extractor(mean + "." + embed[ind], MODEL, TOKENIZER)
            else:
                m_emb = extractor(mean, MODEL)
            score = similarity(m_emb, text_emb)
            if score > mx_score:
                mx_score = score
                mx_m = mean
    return mx_m, mx_score


def pipeline_parallel(text: str, word: str, extractor) -> (str, float):

    text_emb = extractor(text, MODEL, TOKENIZER)
    (meaning, embed) = find_meanings(word)

    mx_m = ""
    mx_score = 0

    with Pool() as pool:
        args = []
        for ind, mean in enumerate(meaning):
            if mean:
                if embed[ind]:
                    args.append((mean + "." + embed[ind],
                                 MODEL, TOKENIZER))
                else:
                    args.append((mean, MODEL))
        m_embs = pool.starmap(extractor, args)

    for ind, emb in enumerate(m_embs):
        score = similarity(emb, text_emb)
        if score > mx_score:
            mx_score = score
            mx_m = emb

    return mx_m, mx_score


def load_vectors():
    global MODEL, TOKENIZER

    conf = current_app.config["MODEL"]
    if conf == "fasttext":
        MODEL = KeyedVectors.load(current_app.config["FASTTEXT"])
    elif conf == "tinybert":
        TOKENIZER = AutoTokenizer.from_pretrained(current_app.config["TINYBERT"])
        MODEL = AutoModel.from_pretrained(current_app.config["TINYBERT"])
    elif conf == "labse":
        TOKENIZER = AutoTokenizer.from_pretrained(current_app.config["LABSE"])
        MODEL = AutoModel.from_pretrained(current_app.config["LABSE"])
    else:
        MODEL = KeyedVectors.load(current_app.config["FASTTEXT"])


def main(text, word):
    conf = current_app.config["MODEL"]

    if conf == "fasttext":
        return pipeline(text, word, extractor=fasttext)
    if conf == "tinybert":
        return pipeline(text, word, extractor=tiny_bert)
    if conf == "labse":
        return pipeline(text, word, extractor=labse)
