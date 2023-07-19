import sys
input = sys.stdin.readline
inf = int(1e9) # 10억(무한 의미)

n,m = map(int,input().split()) # n: 노드의 개수/ m: 간선의 개수

start = int(input()) # 시작 노드번호

graph = [[] for i in range(n+1)] # 각 노드에 연결돼 있는 노드에 대한 정보를 담는 리스트
# n+1 로 range 설정하여, 노드 번호를 인덱스로 하여 바로 리스트에 접근 가능

visited = [False] * (n+1) # 방문한 적이 있었는지 체크하는 목적의 리스트

distance = [inf] * (n+1) # 최단거리 테이블 모두 무한으로 초기화


# 모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int,input().split()) 
    graph[a].append((b,c)) # a번 노드에서  b번 노드로 가는 비용이 c라는 뜻


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = inf
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]: 
            # i번째 노드를 방문하지 않았고, inf로 초기화한 min_value보다 distance[i] 가 작다면
            min_value = distance[i] # min_value 갱신
            index = i # index도 노드 번호로 갱신
    return index 

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # j[0]은 start에서 갈 수있는 노드. j[1]은 그때의 비용
        distance[j[0]] = j[1]  
    
    # 시작노드 제외한 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node() # 현재 가장 최단거리가 짧은 노드 꺼내서 방문처리
        visited[now] = True
        # 현재 노드(now)와 연결된 다른 노드 확인 
        for j in graph[now]:
            cost = distance[now] + j[1] # now에서 다른 노드로 가는 비용
            # 만약 cost가 기존 비용보다 작다면 = now를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost # distance[j[0]] 갱신

dijkstra(start)

for i in range(1,n+1): # 모든 노드로 가기 위한 최단거리 출력
    if distance[i] == inf: # 도달할 수 없는 경우 무한 출력
        print("infinity")
    
    else:  # 도달할 수 있는 경우 거리 출력
        print(distance[i]) 