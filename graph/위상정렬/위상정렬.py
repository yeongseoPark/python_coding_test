from collections import deque
from unittest import result

v , e = map(int,input().split()) # 노드의 개수와 간선의 개수 

indegree = [0] * (v+1) # 진입차수 0으로 초기화

graph = [[] for i in range(v+1)] 
# 각 노드에 연결된 간선 정보 담기 위한 연결리스트

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b) # a에서 b로 이동가능

    indegree[b] += 1 # b 진입차수 +=1 

def topology_sort():
    result = []
    q = deque() # 큐 기능 

    for i in range(1,v+1):
        if indegree[i] == 0: # 진입차수 0인 노드들 큐에 삽입 
            q.append(i)

    while q: # 큐가 빌때까지 
        now = q.popleft() # 진입차수 0인 아이들 빼줌
        result.append(now)

        for i in graph[now]: 
            indegree[i] -=1  # now원소와 연결된 노드들 진입차수 -=1

            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()

