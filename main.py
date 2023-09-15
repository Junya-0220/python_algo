# 入力
N = int(input())

# 上の桁から順番に「2 進法に変換した値」を求める
l = [i for i in range(9,-1,-1)] #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# [512,256,128,64,32,16,8,4,2,1] これで割る
# print(l)
for x in l:
	wari = (2 ** x)
	print((N // wari) % 2, end='')

# 最後に改行する
# print("")
print(90 // 512 % 2)
print(90 // 256 % 2)
print(90 // 128 % 2)
print(90 // 64 % 2)
print(90 // 32 % 2)
print(90 // 16 % 2)
print(90 // 8 % 2)
print(90 // 4 % 2)
print(90 // 2 % 2)
print(90 // 1 % 2)
