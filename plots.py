import matplotlib.pyplot as plt

eclat_mean_time =	[0.24806761741638184,	0.5352346658706665,	0.8387587070465088]
declat_mean_time =	[11.719473624229432,	51.654879331588745,	129.98588166236877]
postdiffset_mean_time =[	0.29551937580108645,	0.7136241436004639,	1.1702940702438354]

eclat_std_time = [	0.0036639826904947327,	0.005251450187372836,	0.009618467864039292]
declat_std_time = [	0.16457680531224556,	0.4563109752398956,	0.6037496664571385]
postdiffset_std_time = [	0.0045148502502508694,	0.006948687603762739,	0.013819183994843458]

eclat_mean_memory = [	1.0834104537963867,	1.6346867561340332,	2.0616177558898925]
declat_mean_memory = [	14.459683799743653,	33.5134895324707,	54.03344230651855]
postdiffset_mean_memory = [	5.979916381835937,	17.32505111694336,	36.68019676208496]

eclat_std_memory =	[0.0018074472220008287,	0.002288121715464791,	0.004401695754372103]
declat_std_memory =	[0.0031692938211644052,	0.004936649566774979,	0.0010479680375286957]
postdiffset_std_memory =	[0.0012479507353479627,	0.0012479507353479627,	0.0012363009517630376]

dataset_size = [53, 92, 131]

plt.figure()
plt.errorbar(dataset_size, eclat_mean_time, eclat_std_time)
plt.errorbar(dataset_size, declat_mean_time, declat_std_time)
plt.errorbar(dataset_size, postdiffset_mean_time, postdiffset_std_time)
plt.ylabel('time')
plt.xlabel('dataset size')
plt.yscale("log")
plt.legend(["eclat", "declat", "postdiffset"])
plt.show()

plt.figure()
plt.errorbar(dataset_size, eclat_mean_memory, eclat_std_memory)
plt.errorbar(dataset_size, declat_mean_memory, declat_std_memory)
plt.errorbar(dataset_size, postdiffset_mean_memory, postdiffset_std_memory)
plt.ylabel('memory')
plt.xlabel('dataset size')
plt.yscale("log")
plt.legend(["eclat", "declat", "postdiffset"])
plt.show()
