import re
from textblob import TextBlob
import pandas as pd


def to_lowercase_word(word: str):
    proper_word = word.lower()
    proper_word = re.sub(r"[^a-z0-9]", "", proper_word)
    return proper_word


def extract_nouns(data: list, verbose=False):
    dataset = []
    for tweet in data:
        text_without_link = re.sub(r"http\S+", "", tweet)
        blob = TextBlob(text_without_link)
        nouns = ['NN', 'NNP', 'NNS']
        filtered_tags = [tup[0] for tup in blob.tags if tup[1] in nouns]
        filtered_tags = [to_lowercase_word(word) for word in filtered_tags]
        filtered_tags = [word for word in filtered_tags if word != '']
        filtered_tags = list(dict.fromkeys(filtered_tags))
        dataset.append(filtered_tags)
        if verbose:
            print(tweet)
            print(filtered_tags)
    return dataset


def add_columns_numbers_to_attributes(data: pd.DataFrame):
    for i, col in enumerate(data.columns):
        data.iloc[:, i] = data.iloc[:, i].apply(lambda x: str(i) + x)
    return data
