n = int(input())
arr = list(map(int, input().split()))

dp1 = [1] * n # LIS / dp[i] : arr[i] 를 마지막으로 하는 가장 긴 증가하는 부분 수열
dp2 = [1] * n # LDS / dp[i] : arr[i] 를 시작으로 하는 가장 긴 감소하는 부분 수열
dp3 = [0] * n # 가장 긴 바이토닉 수열

# 인덱스를 끝으로 하는 가장 긴 증가하는 부분수열
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

# i를 시작으로 하는 가장 긴 감소하는 부분수열
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(n):
    dp3[i] = dp1[i] + dp2[i] - 1

print(max(dp3))