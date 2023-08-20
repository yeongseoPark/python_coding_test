from collections import deque

def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

for _ in range(int(input())):
    n = int(input())
    nodes = []
    nodes.append(list(map(int, input().split())))
    for i in range(n):
        nodes.append(list(map(int, input().split())))
    nodes.append(list(map(int, input().split())))
    
    graph = [[] for _ in range(len(nodes))] # 0은 집, 마지막은 락페스티벌
    
    # 편의점이 100개라 n^2으로 모든 가능성 다 따져봐도 10만밖에 안됨
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j:
                if distance(nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1]) <= 1000:
                      graph[i].append(j)
                      graph[j].append(i)
    
    # 연결 정보를 가지고 bfs
    q = deque()
    q.append(0)
    find = 0
    visited = [0] * (n+2)
    visited[0] = True
    
    while q:
        cur = q.popleft()
        cur_x, cur_y = nodes[cur]
        
        if [cur_x, cur_y] == nodes[-1]:
            print("happy")
            find = 1
            break
        
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    if not find:
        print("sad")

