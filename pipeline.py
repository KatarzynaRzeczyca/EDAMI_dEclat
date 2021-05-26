import json
import pandas as pd
from eclat import eclat
from data_preprocessing import extract_nouns

def load_data(file: str, verbose=False):
    with open(file) as json_file:
        data = json.load(json_file)
        tweets = []
        for item in data['tweets']:
            tweets.append(item)
            if verbose:
                print(item)
    return tweets


if __name__ == "__main__":
    data = load_data("tweets.txt")
    raw_dataset = extract_nouns(data)
    dataset = pd.DataFrame(raw_dataset)
    print(dataset)
    frequent_itemsets = eclat(dataset, min_support=3, min_length=3)
    print("\nResult:")
    print(frequent_itemsets)
