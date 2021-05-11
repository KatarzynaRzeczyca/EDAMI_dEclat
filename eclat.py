import pandas as pd


class Tidlist:
    def __init__(self):
        self.keys = []
        self.values = []
        self.size = 0

    def put(self, key, value):
        if key in self.keys:
            self.values[self.keys.index(key)].add(value)
        else:
            self.keys.append(key)
            self.values.append({value})
            self.size += 1

    def put_all(self, key, values: set):
        if key in self.keys:
            self.values[self.keys.index(key)].union(values)
        else:
            self.keys.append(key)
            self.values.append(values)
            self.size += 1

    def get(self, key):
        if key in self.keys:
            return self.values[self.keys.index(key)]
        else:
            return {}

    def remove_not_frequent_items(self, min_sup):
        indexes_of_items_to_remove = []
        for i in range(self.size):
            if len(self.values[i]) < min_sup:
                indexes_of_items_to_remove.append(i)
        for i in reversed(indexes_of_items_to_remove):
            del self.keys[i]
            del self.values[i]
        self.size -= len(indexes_of_items_to_remove)

    def concatenate(self, another):
        for i in range(another.size):
            self.put_all(another.keys[i], another.values[i])

    def __str__(self):
        result = ""
        for i in range(self.size):
            result += ": ".join(['[' + ','.join(self.keys[i]) + ']', ','.join(str(e) for e in self.values[i]) + "\n"])
        result += "size: " + str(self.size)
        return result


def create_tidlist_from_data(df: pd.DataFrame):
    result = Tidlist()
    i = 0
    for row in df.iloc:
        for item in row:
            if not pd.isna(item):
                result.put([item], i)
        i += 1
    return result


def is_different_in_last_item(list1: list, list2: list):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1) - 1):
        if list1[i] != list2[i]:
            return False
    return list1[-1] != list2[-1]


def compute_next_level(previous: Tidlist):
    next_level = Tidlist()
    for i in range(previous.size - 1):
        for j in range(i + 1, previous.size):
            if is_different_in_last_item(previous.keys[i], previous.keys[j]):
                new_key = list(set(previous.keys[i]) | set(previous.keys[j]))
                new_key.sort()
                new_val = previous.values[i] & previous.values[j]
                if len(new_val) > 0:
                    next_level.put_all(new_key, new_val)
            else:
                break
    return next_level


def eclat(df: pd.DataFrame, min_support=1, min_length=1, verbose=False):
    result = Tidlist()
    tidlist = create_tidlist_from_data(df)
    itemset_length = 1
    if verbose and tidlist.size == 0:
        print("Dataset empty or corrupted")
    while tidlist.size > 0:
        if verbose:
            print("Itemset length=" + str(itemset_length) + ":\n" + str(tidlist))
        tidlist.remove_not_frequent_items(min_support)
        if verbose:
            print("After reduction:\n" + str(tidlist))
        if itemset_length >= min_length:
            result.concatenate(tidlist)
        tidlist = compute_next_level(tidlist)
        itemset_length += 1
    return result


if __name__ == "__main__":
    data = pd.read_csv("input.csv", header=None)
    frequent_itemsets = eclat(data, verbose=True, min_length=2, min_support=2)
    print("\nResult:")
    print(frequent_itemsets)



