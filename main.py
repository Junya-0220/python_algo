"""

i=1,2,3,…,Q それぞれについて，
アタリの方が多い場合 win を，
ハズレの方が多い場合 lose を，
アタリとハズレが同じ場合 draw を，一行ずつ，総計 Q 行に出力してください．

入力
7
0 1 1 0 1 0 0
3
2 5
2 7
5 7

出力
win
draw
lose

"""

# 入力
N = int(input())
# この書き方覚えておいた方がいいかもね list関数を使って、map関数でintを指定し、
# 最終的に数値の配列が標準入力から取得できる
A = list(map(int, input().split()))
Q = int(input())
L = [ None ] * Q
R = [ None ] * Q
for i in range(Q):
	L[i], R[i] = map(int, input().split())

# アタリの個数・ハズレの個数の累積和を求める
# 配列 A が 0 番目から始まっていることに注意！
Atari = [ 0 ] * (N + 1)
Hazre = [ 0 ] * (N + 1)
for i in range(1, N+1):
	# アタリについて計算
	Atari[i] = Atari[i - 1]
	if A[i - 1] == 1:
		Atari[i] += 1
	# ハズレについて計算
	Hazre[i] = Hazre[i - 1]
	if A[i - 1] == 0:
		Hazre[i] += 1

# 質問に答える
for i in range(Q):
	NumAtari = Atari[R[i]] - Atari[L[i] - 1]
	NumHazre = Hazre[R[i]] - Hazre[L[i] - 1]
	if NumAtari > NumHazre:
		print("win")
	elif NumAtari == NumHazre:
		print("draw")
	else:
		print("lose")
