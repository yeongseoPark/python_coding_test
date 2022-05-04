# 1~n 까지의 도시, m개의 단방향 도로
# 모든 도로의 거리는 1
# 특정한 도시 x로부터 출발하여 도달할 수 있는 모든 도시 중,
# 최단 거리가 정확히 k인 모든 도시의 번호 출력
# 이때 x에서 x로 가는 최단거리는 항상 0
# 도달할 수있는 도시 중 최단거리 k인 도시 하나도 없으면 -1출력
from collections import deque

n, m, k, x = map(int,input().split()) # 도시 개수 n / 도로 개수 m / 최단거리 k / 출발 도시 x
graph = [[] for _ in range(n+1)] 

# 도로 정보 입력받기. 인덱스가 시작 도시, 인덱스 해당하는 리스트 안의 인자가 도착 도시
for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b) 

distance    = [-1] * (n+1) # 모든 도시에 대한 최단 거리 초기화 #얘가 왜있는건지..
distance[x] = 0 # 출발 도시까지 거리는 0 

#BFS
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시들 for문 돌림
    for next_node in graph[now]:
        # 아직방문하지 않은 도시라면,
        if distance[next_node] == -1:
            # 최단 거리 갱신...????
            distance[next_node] = distance[now]+1
            q.append(next_node) # 이 방문하지 않은 next_node들을 스택에 넣고, 여기서 다시 while문 실행해서 그 도시의 next_node들 살펴보는 구조
            # distance는 bfs를 실행하며 node를 타고 들어갈 수록 커짐(distance[now]에 1씩 더하니까)


# 최단 거리가 k인 모든 도시 번호를 오름차순으로 출력
check = False #...?
for i in range(1,n+1): # 자기부터~마지막 도시
    if distance[i] == k: # 출발도시 부터의 거리가 k라면 
        print(i)
        check = True # True로 바꿔서 -1출력 안되게 함

if check == False:
    print(-1)






# def bfs(data, x, visited):
#     queue = deque()
#     queue.append(x)

#     linked_city = []
#     for i in range(len(data)):
#         if data[i][0] == x:
#             linked_city.append(data[i])

#     while queue:
#         x = queue.popleft()
#         for i in linked_city:  # queue에 인접 도시들 삽입
#             queue.append(i[1]) 

        






# def dfs(data, x, visited): #끝까지 탐색하는게 아니라, k에 해당하는 도시 개수 세는거니깐 bfs가 맞나...?
#     visited[x]   = True
#     print(x, end = ' ')

#     linked_city = []
#     for i in range(len(data)):
#         if data[i][0] == x:
#             linked_city.append(data[i])

#     for i in range(len(linked_city)):
#         if not visited[linked_city[i][1]]:
#             dfs(data, linked_city[i][1], visited)  #끝에 다다라서 linked_city가 없다면 None을 리턴

# visited = [False] * (n+1) #n일시 n번째가 없어서 list outofindex남
# dfs(data, x, visited)



    # stack = []
    # relevean_list = []
    # count = []
    # for i in data:
    #     if i[0] == x:
    #         relevean_list.append(i)

    # if relevean_list == None: # base case
    #     count.append()
    #     return stack
    
    # for j in relevean_list:
    #     stack.append(j[1])
    #     dfs(data,j)


