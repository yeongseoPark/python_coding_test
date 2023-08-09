n = int(input())

prices = [0] + list(map(int, input().split()))

dp = [0] + [prices[1]] + [0] * (n-1)

for i in range(1, n+1):
    maxed = -1
    for j in range(1, i+1):
        maxed = max(maxed, dp[i-j] + prices[j])
    
    dp[i] = maxed

print(dp[n])