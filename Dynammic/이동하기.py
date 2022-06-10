# https://www.acmicpc.net/problem/11048

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dp = [[0] * (m+1) for _ in range(n+1)] # 왼쪽, 위 첫번째줄도 점화식에 따라 계산해줘야 하기 때문에 한칸씩 더 크게 만듬
miro = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = miro[i-1][j-1] + max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        # dp테이블이 miro테이블보다 한칸씩 더 크기때문에 miro[i-1][j-1]에 dp의 max값 더해주면 된다.

print(dp[-1][-1])

