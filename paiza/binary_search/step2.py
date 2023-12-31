"""
整数 n と、数列 a_1, ... , a_n と、整数 k が与えられます。

整数 k が数列の何番目にあるかを求めてください。なお、最初の要素 (a_1) を 1 番目とします。

ただし、数列に整数 k が含まれていない場合は、0 を出力してください。

また、数列に整数 k が複数含まれている場合は、数列を先頭から順に見たときに最初に現れる k が数列の何番目にあるかを求めてください。

入力される値
n
a_1 a_2 ... a_n
k

・ 1行目に、数列の長さを表す整数 n が与えられます。
・ 2行目に、数列の値 a_i が半角スペース区切りで与えられます。
・ 3行目に、整数 k が与えられます

入力例1
5
-3 2 0 -1 2
2
"""

n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

index_of_k = -1

for i in range(n):
    if a[i] == k:
        index_of_k = i 
        break

print(index_of_k + 1)