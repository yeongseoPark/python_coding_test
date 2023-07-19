import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

# 노드의 개수 n / 간선의 개수 m
n,m = map(int,input().split())

start = int(input()) # 시작 노드 번호

graph = [[] for i in range(n+1)]# 각 노드(인덱스) 에 연결돼 있는 노드에 대한 정보 담는 리스트
# n+1로, 인덱스값과 실제 노드번호가 일치하도록 해줌 

distance = [inf] * (n+1) # 최단거리 테이블 무한으로 초기화

 # 모든 간선의 개수 입력받기 
for i in range(m):
    a, b , c = map(int,input().split())
    graph[a].append((b,c))
  # a 에서 b노드로 가는 비용 c

def dijkstra(start):
    q = []
     # heapq 라이브러리를 사용하기 위해서는 그냥 빈 리스트를 생성해놓은 다음
     # heapq모듈의 함수를 호출할 때마다 이 리스트(q)를 인자로 넘겨야 함 

    heapq.heappush(q, (0,start))
    distance[start] = 0
    # 파이썬에서는 heapq모듈을 사용하여 원소를 추가하거나 삭제한 리스트가 바로 최소 힙
    # 시작 노드로 가기 위한 최단 경로는 0, 이를 heappush를 이용하여 q에 인자 추가
    
    while q: 
     # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
         # heappop: 가장 작은 원소를 삭제 후, 그 값을 리턴

        if distance[now] < dist:
            continue
        
             # 이미 처리된 적 있어서, 최단거리테이블에 있는 값이 heappop으로 꺼낸 거리보다 짧다면 무시

        for i in graph[now]:
          # 현재 노드에 맞닿은 다른 노드들 확인

            cost = dist + i[1]
            # i[1]은 이동하는 비용

            if cost < distance[i[0]]:
             # 만약 cost가 최단 거리 테이블의 기존 최단거리보다 짧다면 
                distance[i[0]] = cost
                 # 최단거리 테이블 업데이트 해주고
                
                heapq.heappush(q, (cost, i[0]))
                 # 이를 heapq에 (최단거리, 맞닿는노드)로 넣어줌

dijkstra(start)


# 모든 노드로 가기 위한 최단거리 출력, 인덱스와 노드번호 같기에 1부터 시작
for i in range(1, n+1):
    if distance[i] == inf:
        print("infinity")
    # 도달할 수 없으면 infinity 출력 
    else:
        print(distance[i])

 # 도달할 수 있으면 거리 출력




    
