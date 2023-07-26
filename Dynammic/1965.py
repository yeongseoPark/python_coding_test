n = int(input())
seq = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j]+1)
            # seq[i]를 사용하지 않고 현재까지 만들어진 가장 긴 부분 수열의 길이
            # seq[j]를 마지막으로 사용하는 부분 수열에 seq[i]를 추가한 길이

print(max(dp))