n = int(input())
seq = list(map(int, input().split()))

# dp[i][j] : seq의 처음 i개의 수와, seq의 끝 j개의 수가 만들 수 있는
# 가장 긴 팰린드롬의 길이를 저장
dp = [[0] * (n+1) for i in range(n+1)]

# seq[-i]와 seq[j-1]이 같다면 팰린드롬의 일부로 사용 가능함
for i in range(1, n+1):
    for j in range(1, n+1):
        if seq[-i] == seq[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # seq[-i]와 seq[j-1]이 다르다면, 둘 중 하나만 팰린드롬의 일부로 사용 가능
        # 따라서 둘 중 더 큰 값을 선택
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# 원래 수열의 길이 n에서 가장 긴 팰린드롬의 길이 dp[n][n]을 뺌
# 이 값이 팰린드롬을 만들기 위해 필요한 최소한의 수의 개수
print(n-dp[n][n])
        