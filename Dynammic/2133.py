n = int(input())

dp = [0] * (31)
dp[0] = 0
dp[1] = 0
dp[2] = 3

for i in range(4, n+1):
    if i % 2 == 0:
        dp[i] += dp[i-2] * 3

        for j in range(i-4, -1 ,-2):
            dp[i] += dp[j] * 2
        
        dp[i] += 2 # 특수한 모양 두개

print(dp[n])