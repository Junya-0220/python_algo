"""
累積和を求めてから、対象の期間の累計を出力する。

入力例
10 5
8 6 9 1 2 1 10 100 1000 10000
2 3
1 4
3 9
6 8
1 10

出力例
15
24
1123
111
11137
"""

# Nが全体の集計日,Qが集計した日から対象の期間を抜き出す回数
N, Q = map(int, input().split())
# Aは日毎の来場者数
A = list(map(int, input().split()))
L = [ None ] * Q # Noneという要素を初期化で入れている
R = [ None ] * Q
for j in range(Q):
	L[j], R[j] = map(int, input().split())

# print(L)
# print(R)

# Nが全体の集計日に対して、それに１を追加した配列Sを用意する
S = [ None ] * (N + 1)

# Sの添字0に対して、0を代入する。
S[0] = 0
# 累積和を計算している最終的にSに累積和が取得できる
for i in range(N):
	# S[i + 1]からスタートすることで、S[0]に対しては代入していない
	S[i + 1] = S[i] + A[i]

# 対象の期間分ループを回す
for j in range(Q):
	print(S[R[j]] - S[L[j] - 1])