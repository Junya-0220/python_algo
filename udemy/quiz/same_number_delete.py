"""
input X:[1,2,3,4,4,5,5,8,10] Y:[4,5,5,5,6,7,8,8,10]
=>    X:[1,2,3,4,4,10]       Y:[5,5,5,6,7,8,8,10]
"""

from typing import List 
from collections import Counter

def min_count_remove(x: List[int], y: List[int]) -> None:
    # count_x = {}
    # count_y = {}
    # for i in x:
    #     count_x[i] = count_x.get(i,0) + 1
    # for i in y:
    #     count_y[i] = count_y.get(i,0) + 1

    # print(count_x)
    # print(count_y)
    counter_x = Counter(x)
    counter_y = Counter(y)
    # print(counter_x)
    # print(counter_y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]

x = [1,2,3,4,4,5,5,8,10]
y = [4,5,5,5,6,7,8,8,10]
print('x = ',x)
print('y = ',y)
min_count_remove(x,y)
print('x = ',x)
print('y = ',y)