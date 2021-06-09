from pyvis.network import Network
from matplotlib import cm
import math


def double_to_hex(number):
    number = math.floor(number * 255)
    return "{:02x}".format(number)


def rgba_to_hex(rgba):
    return '#' + double_to_hex(rgba[0]) + double_to_hex(rgba[1]) + double_to_hex(rgba[2])


def get_color_from_palette(palette, coefficient):
    color_map = cm.get_cmap(palette)
    color = color_map(coefficient)
    return rgba_to_hex(color)


class FaPlot:
    def __init__(self, size_x=1000, size_y=1000, directed=False, palette='Blues', item_color='#00aa11',
                 max_node_size=20.0, min_node_size=4, item_node_size=5.0, maximum_support=1.0):
        self.net = Network(str(size_x) + 'px', str(size_y) + 'px', directed=directed)
        self.palette = palette
        self.item_color = item_color
        self.max_node_size = max_node_size
        self.min_node_size = min_node_size
        self.item_node_size = item_node_size
        self.maximum_support = maximum_support
        self.itemset_index = 0

    def add_item(self, list_of_items, relative_support):
        node_id = self.itemset_index
        self.itemset_index += 1
        node_name = '{0:.2f}'.format(relative_support * 100) + '%'
        node_size = max(relative_support * 20 / self.maximum_support, self.min_node_size)
        node_color = get_color_from_palette(self.palette, relative_support / self.maximum_support)
        self.net.add_node(node_id, label=node_name, size=node_size, color=node_color)
        for item in list_of_items:
            self.net.add_node(item, size=self.item_node_size, color=self.item_color)
            self.net.add_edge(item, node_id)

    def show_graph(self, file_name='nx.html'):
        self.net.show(file_name)


if __name__ == '__main__':
    graph = FaPlot(maximum_support=0.5)
    graph.add_item(['a1', 'a2', 'a3', 'a4'], 0.5)
    graph.add_item(['a5', 'a6', 'a3', 'a4'], 0.1)
    graph.add_item(['a5', 'a6', 'a3'], 0.01)
    graph.show_graph()
