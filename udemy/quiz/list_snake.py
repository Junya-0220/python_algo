from typing import List

def snake_string_v1(chars: str) -> List[List[str]]:
    result = [[],[],[]]
    result_index = {0,1,2}
    insert_index = 1
    for i,s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_index - {insert_index}:
            result[rest_index].append(' ')
    return result

def snake_string_v2(chars:str, depth:int) -> List[List[str]]:
    result = [[] for i in range(depth)]
    result_index = {i for i in range(depth)}
    insert_index = int(depth / 2)


    def pos(i):
        return i + 1
    
    def neg(i):
        return i - 1
    
    op = neg 

    for s in chars:
        result[insert_index].append(s)
        for rest_index in result_index - {insert_index}:
            result[rest_index].append(' ')
        if insert_index <= 0:
            op = pos 
        if insert_index >= depth - 1:
            op = neg
        insert_index = op(insert_index)
    return result 

# numbers = [str(i) for j in range(5) for i in range(10)]
# strings = ''.join(numbers)
# for line in snake_string_v1(strings):    
#     print(''.join(line))

import string 
alphabet = [s for _ in range(2) for s in string.ascii_lowercase]
strings = ''.join(alphabet)
for line in snake_string_v2(strings, 6):
    print(''.join(line))