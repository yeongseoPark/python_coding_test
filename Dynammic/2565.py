number = int(input())

lines = []
for _ in range(number):
    a,b = map(int, input().split())
    lines.append((a,b))

lines.sort(key= lambda x: x[0]) # 왼쪽 기준 오름차순 정렬
"""
남아있는 모든 전깃줄이 서로 교차하지 않게 없애야 하는 전깃줄의 최소 개수
= (전체 전깃줄 개수 - 교차하지 않는 전깃줄의 최대 개수)
"""
# 우측 전깃줄의 LIS구해주면 됨
right = [x[1] for x in lines]
dp = [1] * number

for i in range(number):
    for j in range(i):
        if right[i] > right[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(number - max(dp))