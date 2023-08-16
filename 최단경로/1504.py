import heapq
import sys

n, e = map(int, input().split()) # 정점 N개와 간선의 개수 E개

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b)) # a에서 b까지의 양방향 길, 거리는 c
    graph[b].append((c, a))
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [sys.maxsize] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (distance[start], start))

    while q:
        cur_dist, cur_position = heapq.heappop(q)
        
        if distance[cur_position] < cur_dist:
            continue
        
        for cost, dist in graph[cur_position]:
            new_distance = cur_dist + cost
            if new_distance < distance[dist]:
                distance[dist] = new_distance
                heapq.heappush(q, (new_distance, dist))

    return distance


ndistance = dijkstra(1)
v1distance = dijkstra(v1)
v2distance = dijkstra(v2)

answer = min(ndistance[v1] + v1distance[v2] + v2distance[n], ndistance[v2] + v2distance[v1] + v1distance[n])

if answer >= sys.maxsize:
    print(-1)
else:
    print(answer)