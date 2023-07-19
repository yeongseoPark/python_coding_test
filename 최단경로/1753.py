import heapq, sys

vertex, edge = map(int, input().split())

start = int(input())

graph = [dict() for _ in range(vertex+1)] # 간선의 개수가 많아서, 2중리스트로하면은 최소값 비교하다 시간초과 날듯
"""
[
    idx 0 : {}
    idx 1 : {2번 노드 : (가중치, 2번노드)} -> 1번노드에서 2번노드로 가중치만큼의 간선이 있음
    .
    .
]
"""
for _ in range(edge):
    u ,v ,w = map(int, input().split()) # u -> v인 가중치 w의 간선
    if graph[u].get(v) is not None: # 이미 u->v 가 있는경우 값 비교
        if w < graph[u].get(v)[0]:
            graph[u][v] = (w,v)
            continue
        else:
            continue
    else:
        graph[u][v] = (w,v)

queue = []
heapq.heappush(queue, (0,start))

dist = [(sys.maxsize - 1) for _ in range(vertex+1)]
dist[start] = 0 

while queue:
    value, node = heapq.heappop(queue)

    if value > dist[node]:
        continue
    
    for i in graph[node].keys():
        if value + graph[node][i][0] < dist[i]:
            dist[i] = value + graph[node][i][0]
            heapq.heappush(queue, (value + graph[node][i][0], i))

# 최단경로배열 출력
for i in dist[1:]:
    if i == sys.maxsize - 1:
        print("INF")
    else:
        print(i)


