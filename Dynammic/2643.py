n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

# 종이들을 가로 혹은 세로 길이가 긴 순서대로 정렬, 만약 max(x)가 같다면 min(x)를 기준으로 내림차순 정렬
papers.sort(key=lambda x: (max(x), min(x)), reverse=True)

# 종이 i를 꼭대기에 두었을때의 최대 높이
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # 현재 종이가 이전 종이 위에 올라갈 수 있는지 확인
        if max(papers[j]) >= max(papers[i]) and min(papers[j]) >= min(papers[i]):
            dp[i] = max(dp[i], dp[j] + 1)
            # dp[j] + 1 : j번째 종위를 맨 위에 두었을 때의 최대 높이에 현재 종이 i를 추가, dp[i] : i번째 종이를 맨 위에 두었을때 높이.
            # 이 둘을 비교

print(max(dp))
