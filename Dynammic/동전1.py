# https://www.acmicpc.net/problem/2293

from sys import stdin

input = stdin.readline

n,k = map(int,input().split()) # 종류 n가지, 가치의 합 k

coins = [int(input()) for _ in range(n)] # 코인의 종류

dp = [0 for _ in range(k+1)]
# 동전 한개만 쓸때의 경우의 수 
dp[0] = 1

for i in coins: # i원짜리 동전
    for j in range(i,k+1): # i부터 ~ k까지 범위의 가치의 합 j
        dp[j] += dp[j-i] # j를 만드는 경우의 수 : dp[j] += dp[j-k]

print(dp[k])


# 점화식: 하나씩 동전을 추가시키고, t원짜리 동전을 추가할 때 f(k) += f(k-t)
