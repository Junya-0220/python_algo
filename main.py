import itertools

original_list = [11, 46, 47, 77, 80]
cumulative_sum = list(itertools.accumulate(original_list))
print(cumulative_sum)
