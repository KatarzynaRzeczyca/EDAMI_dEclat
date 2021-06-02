import pandas as pd
import eclat as ec

from declat import Diffset, declat_from_diffsets
from eclat import Tidlist, create_tidlist_from_data


def eclat_one_loop_with_infrequent(df: pd.DataFrame, min_support=1, min_length = 1, verbose=False):
    result = Tidlist()
    tidlist = create_tidlist_from_data(df)
    values_initial = tidlist.values.copy()
    if verbose and tidlist.size == 0:
        print("Dataset empty or corrupted")
    if verbose:
        print(str(tidlist))
    tidlist.remove_not_frequent_items(min_support)
    if verbose:
        print("After reduction:\n" + str(tidlist))
    if len(tidlist.keys[0]) >= min_length:
        result.concatenate(tidlist)
    tidlist = ec.compute_next_level(tidlist)
    return tidlist, values_initial, result


def tidlist_to_diffset(tidlist: Tidlist, old_values: [], first_loop_result: Tidlist):
    result = Diffset()
    diffsets = []
    support = []
    all_tid_set = set()

    for id in range(len(old_values)):
        for v in old_values[id]:
            all_tid_set.add(v)

    for id in range(tidlist.size):
        temp_values = set()
        for tid in all_tid_set:
            if tid not in tidlist.values[id]:
                temp_values.add(tid)
        diffsets.append(temp_values.copy())
        support.append(len(tidlist.values[id]))

    result.values = diffsets
    result.keys = tidlist.keys
    result.size = tidlist.size
    result.support = support

    return result


def postdiffset(df: pd.DataFrame, min_support=1, min_length=1, verbose=False):
    tidlists_collection, keys_initial, first_loop_result = eclat_one_loop_with_infrequent(df, min_support, verbose)
    diffsets_collection = tidlist_to_diffset(tidlists_collection, keys_initial, first_loop_result)
    result_init = Diffset()
    result_init.concatenate_tidlist(first_loop_result)
    result = declat_from_diffsets(diffsets_collection, result_init, min_support, min_length, verbose)
    return result


if __name__ == "__main__":
    data = pd.read_csv("input.csv", header=None)
    # data = pd.read_csv("mushrooms.csv")
    # data = add_columns_numbers_to_attributes(data)
    print(data)
    frequent_itemsets = postdiffset(data, verbose=True, min_length=1, min_support=1)
    print("\nResult:")
    print(frequent_itemsets)
