import json
import pandas as pd
from eclat import eclat
from declat import declat
from data_preprocessing import extract_nouns
import tracemalloc
import time
import numpy as np
import os

from postdiffset import postdiffset


def load_data(file: str, verbose=False):
    with open(file) as json_file:
        data = json.load(json_file)
        tweets = []
        for item in data['tweets']:
            tweets.append(item)
            if verbose:
                print(item)
    return tweets


def run_test(function, dataset, **kwargs):
    tracemalloc.start()
    start = time.time()
    function(dataset, **kwargs)
    end = time.time()
    ignored, memory_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    elapsed_time = end - start
    return elapsed_time, memory_peak


def run_n_of_tests(function, dataset, n_of_tests, verbose=False, **kwargs):
    result = pd.DataFrame(index=range(n_of_tests), columns=['time', 'memory'])
    for i in range(n_of_tests):
        if verbose:
            print("Starting test no:", i)
        time, memory = run_test(function, dataset, **kwargs)
        memory /= 2 ** 20 # in MB
        result.loc[i, :] = [time, memory]
        if verbose:
            print(f"Result: time:{time}s, memory:{memory}MB")
    return result


def run_and_save_resource_test(dataset, n_of_tests, result_file_name_prefix: str, verbose=False, min_length=1, min_support=1):
    print(20*'#', 'eclat', 20*'#')
    result_eclat = run_n_of_tests(eclat, dataset, n_of_tests, verbose=verbose, min_length=min_length, min_support=min_support)
    print(20*'#', 'declat', 20*'#')
    result_declat = run_n_of_tests(declat, dataset, n_of_tests, verbose=verbose, min_length=min_length, min_support=min_support)
    print(20 * '#', 'postdiffset', 20 * '#')
    result_postdiffset = run_n_of_tests(postdiffset, dataset, n_of_tests, verbose=verbose, min_length=min_length, min_support=min_support)
    result = pd.concat([result_eclat.add_prefix('eclat_'), result_declat.add_prefix('declat_'), result_postdiffset.add_prefix('postdiffset_')], axis=1)
    means = np.mean(result, axis=0)
    std_devs = np.std(result, axis=0)
    result.loc['mean', :] = means
    result.loc['std_dev', :] = std_devs
    if verbose:
        print("Result:")
        print(result)
    result.to_csv(result_file_name_prefix + '_l' + str(min_length) + '_s' + str(min_support) + '.csv')


if __name__ == "__main__":
    # results folder creation
    results_dir = 'results'
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)
    # dataset preparation
    data = load_data("tweets.txt")
    raw_dataset = extract_nouns(data)
    dataset = pd.DataFrame(raw_dataset)
    # calculations
    print(dataset)
    run_and_save_resource_test(dataset, 10, '/'.join([results_dir, 'tweets']), verbose=True)

