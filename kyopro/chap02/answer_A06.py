"""
累積和を求めてから、対象の期間の累計を出力する。

"""

N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [ None ] * Q # Noneという要素を初期化で入れている
R = [ None ] * Q
for j in range(Q):
	L[j], R[j] = map(int, input().split())
 
S = [ None ] * (N + 1)
S[0] = 0
for i in range(N):
	S[i + 1] = S[i] + A[i]
 
for j in range(Q):
	print(S[R[j]] - S[L[j] - 1])

# ライブラリを使って計算するとこんな感じ

import itertools

original_list = [11, 46, 47, 77, 80]
cumulative_sum = list(itertools.accumulate(original_list))
print(cumulative_sum)
