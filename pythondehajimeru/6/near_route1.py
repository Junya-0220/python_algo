m,n = 6,5

route = [[0 for i in range(n+1)] for j in range(m+1)]

for i in range(m+1):
    route[i][0] = 1

for i in range(1,n +1):
    route[0][i] = 1
    for j in range(1,m+1):
        route[j][i] = route[j-1][i] + route[j][i-1]

print(route[m][n])