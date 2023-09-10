"""
[1] => [2] => 2
[2,3] => [2,4] => 24
[8,9] => [9,0] => 90
[1,2,3] => [1,2,4] => 124
[7,8,9] => [7,9,0] => 790
[9,9,9] => [1,0,0,0] => 1000
[9,9,9,9] => [1,0,0,0,0] => 10000

"""

# l =[1,2,3]
# print(int(''.join([str(i) for i in l])) + 1)

from typing import List 

def list_to_int_plus_one(numbers: List[int]) -> int:
    i = len(numbers) -1
    numbers[i] += 1