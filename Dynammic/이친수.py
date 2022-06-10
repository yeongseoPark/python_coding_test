# https://www.acmicpc.net/problem/2193

n = int(input())

# 1의자리 1개, 2의자리 1개, 3의자리 2개 , 4의자리 3개, 5의자리 5개 , 6의자리 8개 -> 5의자리 부터 n-1번째 + n-2번째 

dp = [1,1,2,3]

for i in range(4,90):
    dp.append(dp[i-2] + dp[i-1])

print(dp[n-1])

