"""
入力される値
n
a_1 a_2 ... a_n
k

・ 1行目に、数列の長さを表す整数 n が与えられます。
・ 2行目に、数列の値 a_i が半角スペース区切りで与えられます。
・ 3行目に、整数 k が与えられます。

入力例1
5
-3 2 0 -1 2
2

出力例1
2
"""

n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

num_of_k = 0
for val in a:
    if val == k:
        num_of_k += 1

print(num_of_k)