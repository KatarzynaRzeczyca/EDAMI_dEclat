from pipeline import load_data
import pandas as pd
from eclat import eclat
from declat import declat
from data_preprocessing import extract_nouns
from graphs_visualization import FaPlot

if __name__ == "__main__":
    data = load_data("tweets131.txt")
    raw_dataset = extract_nouns(data)
    dataset = pd.DataFrame(raw_dataset)
    frequent_itemsets = declat(dataset, verbose=False, min_length=3, min_support=3)
    number_of_items_to_present = 34
    iteration_range = min(number_of_items_to_present, frequent_itemsets.size)
    maximum_support = 0.0
    for i in range(iteration_range):
        if maximum_support < frequent_itemsets.get_support(i):
            maximum_support = frequent_itemsets.get_support(i)
    maximum_support = maximum_support / dataset.shape[0]
    graph_plot = FaPlot(maximum_support=maximum_support)
    for i in range(iteration_range):
        graph_plot.add_item(frequent_itemsets.get_key(i), frequent_itemsets.get_support(i) / dataset.shape[0])
    graph_plot.show_graph('n2.html')
    print(frequent_itemsets)
