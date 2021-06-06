import matplotlib.pyplot as plt


class PlotData:
    def __init__(self, x_data, y_data, errorbars):
        self.x_data = x_data
        self.y_data = y_data
        self.errorbars = errorbars



def plot_with_errorbars(plot_data_list, y_label, x_label, scale, legend, title):
    plt.figure()
    for data in plot_data_list:
        plt.errorbar(data.x_data, data.y_data, data.errorbars)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.yscale(scale)
    plt.legend(legend)
    plt.title(title)
    plt.show()


dataset_size = [53, 92, 131]

# TWEETS - time

eclat_mean_time = [0.24806761741638184, 0.5352346658706665, 0.8387587070465088]
declat_mean_time = [11.719473624229432, 51.654879331588745, 129.98588166236877]
postdiffset_mean_time = [0.29551937580108645, 0.7136241436004639, 1.1702940702438354]

eclat_std_time = [0.0036639826904947327, 0.005251450187372836, 0.009618467864039292]
declat_std_time = [0.16457680531224556, 0.4563109752398956, 0.6037496664571385]
postdiffset_std_time = [0.0045148502502508694, 0.006948687603762739, 0.013819183994843458]

data_eclat_time = PlotData(dataset_size, eclat_mean_time, eclat_std_time)
data_declat_time = PlotData(dataset_size, declat_mean_time, declat_std_time)
data_postdiffset_time = PlotData(dataset_size, postdiffset_mean_time,postdiffset_std_time)

plot_with_errorbars([data_eclat_time, data_declat_time, data_postdiffset_time], "time [s]", "dataset size", "log",
                    ["eclat", "declat", "postdiffset"], "Average runtime - nouns")

# TWEETS - memory

eclat_mean_memory = [1.0834104537963867, 1.6346867561340332, 2.0616177558898925]
declat_mean_memory = [14.459683799743653, 33.5134895324707, 54.03344230651855]
postdiffset_mean_memory = [5.979916381835937, 17.32505111694336, 36.68019676208496]

eclat_std_memory = [0.0018074472220008287, 0.002288121715464791, 0.004401695754372103]
declat_std_memory = [0.0031692938211644052, 0.004936649566774979, 0.0010479680375286957]
postdiffset_std_memory = [0.0012479507353479627, 0.0012479507353479627, 0.0012363009517630376]

data_eclat_memory = PlotData(dataset_size, eclat_mean_memory, eclat_std_memory)
data_declat_memory = PlotData(dataset_size, declat_mean_memory, declat_std_memory)
data_postdiffset_memory = PlotData(dataset_size, postdiffset_mean_memory, postdiffset_std_memory)

plot_with_errorbars([data_eclat_memory, data_declat_memory, data_postdiffset_memory], "memory [MB]", "dataset size", "log",
                    ["eclat", "declat", "postdiffset"], "Average memory usage - nouns")

# MUSHROOMS -time

eclat_mean_time = [153.7708816051483,	198.1473175048828,	206.03465461730957]
declat_mean_time = [201.42602081298827,	271.35389003753664,	255.98077507019042]
postdiffset_mean_time = [200.71272492408752,	255.3059754371643,	255.48657224178314]

eclat_std_time = [1.6936336813604915,	0.3746859291689697,	0.26337751777553314]
declat_std_time = [2.828572922704435,	11.380594379002426,	0.45534192528733825]
postdiffset_std_time = [4.896093750245718,	8.010439443307268,	0.3025613107598975]

data_eclat_time = PlotData(dataset_size, eclat_mean_time, eclat_std_time)
data_declat_time = PlotData(dataset_size, declat_mean_time, declat_std_time)
data_postdiffset_time = PlotData(dataset_size, postdiffset_mean_time,postdiffset_std_time)

plot_with_errorbars([data_eclat_time, data_declat_time, data_postdiffset_time], "time [s]", "dataset size", "log",
                    ["eclat", "declat", "postdiffset"], "Average runtime - mushrooms")

# MUSHROOMS - memory

eclat_mean_memory = [66.20548934936524,	83.50113563537597,	92.566157913208]
declat_mean_memory = [71.22373390197754,	93.5472050666809,	106.29534826278686]
postdiffset_mean_memory = [73.23820838928222,	97.48088874816895,	111.28642845153809]

eclat_std_memory = [0.0015680640008078161,	0.0029324119287948845,	0.000018310546875]
declat_std_memory = [0.002364914101324957,	0.001748014962186253,	0.0019314493759317807]
postdiffset_std_memory = [0.0002540038453116339,	0.00023574829101562502,	0.0016938218098018585]

data_eclat_memory = PlotData(dataset_size, eclat_mean_memory, eclat_std_memory)
data_declat_memory = PlotData(dataset_size, declat_mean_memory, declat_std_memory)
data_postdiffset_memory = PlotData(dataset_size, postdiffset_mean_memory, postdiffset_std_memory)

plot_with_errorbars([data_eclat_memory, data_declat_memory, data_postdiffset_memory], "memory [MB]", "dataset size", "log",
                    ["eclat", "declat", "postdiffset"], "Average memory usage - mushrooms")