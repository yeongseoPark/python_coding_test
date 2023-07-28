import heapq
n,l = map(int, input().split())

pools = [list(map(int, input().split())) for _ in range(n)]
pools.sort(key = lambda x : x[0])

cur = 0 # 웅덩이 덮은 마지막 널빤지 위치
cnt = 0 # 널빤지 개수

for start, end in pools:
    if cur > start:
        start = cur
    while start < end:
        start += l
        cnt += 1
    cur = start

print(cnt)