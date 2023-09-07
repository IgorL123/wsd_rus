from multiprocessing import Pool
from gensim.models import KeyedVectors
from flask import current_app
from transformers import AutoTokenizer, AutoModel
from .embeddings import find_meanings, similarity, fasttext
from .bert import labse, tiny_bert


MODELS = []
TOKENIZERS = []


def pipeline(text: str, word: str, extractor, model_index: int) -> (str, float):

    text_emb = extractor(text, MODELS[model_index], TOKENIZERS[model_index])
    (meaning, embed) = find_meanings(word)

    mx_m = ""
    mx_score = 0
    for ind, mean in enumerate(meaning):
        if mean:
            if embed[ind]:
                m_emb = extractor(mean + "." + embed[ind],
                                  MODELS[model_index],
                                  TOKENIZERS[model_index])
            else:
                m_emb = extractor(mean, MODELS[model_index])
            score = similarity(m_emb, text_emb)
            if score > mx_score:
                mx_score = score
                mx_m = mean
    return mx_m, mx_score


def pipeline_parallel(text: str, word: str, extractor, model_index) -> (str, float):

    text_emb = extractor(text, MODELS[model_index], TOKENIZERS[model_index])
    (meaning, embed) = find_meanings(word)

    mx_m = ""
    mx_score = 0

    with Pool() as pool:
        args = []
        for ind, mean in enumerate(meaning):
            if mean:
                if embed[ind]:
                    args.append((mean + "." + embed[ind],
                                 MODELS[model_index],
                                 TOKENIZERS[model_index]))
                else:
                    args.append((mean, MODELS[model_index]))
        m_embs = pool.starmap(extractor, args)

    for ind, emb in enumerate(m_embs):
        score = similarity(emb, text_emb)
        if score > mx_score:
            mx_score = score
            mx_m = emb

    return mx_m, mx_score


def load_vectors():
    global MODELS, TOKENIZERS

    MODELS.append(KeyedVectors.load(current_app.config["FASTTEXT"]))
    TOKENIZERS.append(None)
    """
    MODELS.append(AutoModel.from_pretrained(current_app.config["TINYBERT"]))
    TOKENIZERS.append(AutoTokenizer.from_pretrained(current_app.config["TINYBERT"]))

    MODELS.append(AutoModel.from_pretrained(current_app.config["LABSE"]))
    TOKENIZERS.append(AutoTokenizer.from_pretrained(current_app.config["LABSE"]))
    """


def main(text, word, model_type):

    if model_type == "fasttext":
        return pipeline(text, word, extractor=fasttext, model_index=0)
    if model_type == "tinybert":
        return pipeline(text, word, extractor=tiny_bert, model_index=1)
    if model_type == "labse":
        return pipeline(text, word, extractor=labse, model_index=2)
