from helper_classes import Solution
from helper_functions import order_dict_by_key

data_list = Solution('ex_1_data.txt').read_dataset()
dna_count = order_dict_by_key({i: data_list.count(i) for i in data_list})
for i in dna_count:
    print(i[1], end=' ')
