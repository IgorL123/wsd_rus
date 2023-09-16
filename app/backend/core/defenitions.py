from typing import List
from flask import current_app
import pandas as pd


def find_word(word: str) -> List[str]:
    dtf = pd.read_csv(current_app.config["DEFINITIONS"])
    a = dtf.where(dtf.word == word).dropna(how="all")

    if len(a) == 0:
        return []

    if a["meanings1"]:
        ms = a["meanings1"].values[0].split("', '")
    elif a["meanings2"]:
        ms = a["meanings2"].values[0].split("', '")
    else:
        return []

    ms[0] = ms[0][3:]
    ms[-1] = ms[-1][:-2]

    return ms
