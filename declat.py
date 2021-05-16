from eclat import Tidlist, is_different_in_last_item
import pandas as pd


class Diffset(Tidlist):
    def __init__(self):
        super().__init__()
        # parent itemset's support used in declat
        self.support = []

    def put_empty_if_not_in_set(self, key):
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(set())
            self.size += 1

    def remove_not_frequent_items(self, min_sup):
        indexes_of_items_to_remove = []
        for i in range(self.size):
            if (self.support[i]) < min_sup:
                indexes_of_items_to_remove.append(i)
        for i in reversed(indexes_of_items_to_remove):
            del self.keys[i]
            del self.values[i]
            del self.support[i]
        self.size -= len(indexes_of_items_to_remove)

    def put_all_if_not_in_set(self, key, values: set, support):
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(values)
            self.support.append(support)
            self.size += 1
        else:
            raise ValueError('key cant occur in diffset')

    def concatenate(self, another):
        for i in range(another.size):
            self.put_all_if_not_in_set(another.keys[i], another.values[i], another.support[i])


def create_diffset_from_data(df: pd.DataFrame):
    result = Diffset()
    all_items_set = set()
    i = 0
    for row in df.iloc:
        all_items_left = all_items_set.copy()
        for item in row:
            if not pd.isna(item):
                if [item] not in result.keys:
                    result.put_empty_if_not_in_set([item])
                    for j in range(i):
                        result.put([item], j)
                if item in all_items_left:
                    all_items_left.remove(item)
                all_items_set.add(item)
        for item in all_items_left:
            # items that didn't appear and aren't new
            result.put([item], i)

        i += 1

    # support
    for id in range(result.size):
        result.support.append(i - len(result.values[id]))
    return result


def compute_next_level(previous: Diffset):
    next_level = Diffset()
    for i in range(previous.size - 1):
        for j in range(i + 1, previous.size):
            if is_different_in_last_item(previous.keys[i], previous.keys[j]):
                new_key = list(set(previous.keys[i]) | set(previous.keys[j]))
                new_key.sort()
                new_val = previous.values[j] - previous.values[i]
                new_sup = previous.support[i] - len(new_val)
                next_level.put_all_if_not_in_set(new_key, new_val, new_sup)
            else:
                break
    return next_level


def declat(df: pd.DataFrame, min_support=1, min_length=1):
    result = Diffset()
    diffsets_collection = create_diffset_from_data(df)
    itemset_length = 1
    if diffsets_collection.size == 0:
        raise ValueError('diffsets are empty')
    while diffsets_collection.size > 0:
        diffsets_collection.remove_not_frequent_items(min_support)
        if itemset_length >= min_length:
            result.concatenate(diffsets_collection)
        diffsets_collection = compute_next_level(diffsets_collection)
        itemset_length += 1
    return result


if __name__ == "__main__":
    data = pd.read_csv("mushrooms.csv")
    frequent_itemsets = declat(data)
    print("\nResult:")
    print(frequent_itemsets)
