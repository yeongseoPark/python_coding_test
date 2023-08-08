n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
    # dp[자리수][맨뒤의숫자]

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] # 마지막숫자 0일시 그 전은 1만 가능 
        elif j == 9:
            dp[i][j] = dp[i-1][8] # 마지막숫자 9일시 그 전은 8만 가능
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 


print(sum(dp[n]) % 1000000000)