n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = [triangle[0] + [0 for _ in range(n-1)]]
for i in range(2, n + 1):
    dp.append([0 for _ in range(n)])

for i in range(1, n):
    for j in range(0, i+1):
        if j != 0 and j != n:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        else:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]

print(max(dp[-1])) 