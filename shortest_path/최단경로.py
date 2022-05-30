# https://www.acmicpc.net/problem/1753
import heapq
import sys
sys.setrecursionlimit(10**6) # 파이썬의 기본 재귀 깊이 제한 1000을 확장

input = sys.stdin.readline

inf = int(1e9)

v, e = map(int,input().split())

k = int(input())

graph = [[] for _ in range(v+1)]

distance = [inf] * (v+1)

for i in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) # u에서 v로 가는 비용 w인 간선이 존재한다는 뜻 # 두 정점사이에 여러 간선 존재가능 

def dijkstra(k):
    q = []

    heapq.heappush(q, (0,k))
    distance[k] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(k)


for i in range(1, v+2):
    # if i == k:
    #     print(0)
    if distance[i] != inf:
        print(distance[i])
    else:
        print("INF")


