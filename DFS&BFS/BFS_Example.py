from collections import deque #queue자료구조 라이브러리

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start]= True #현재노드 방문 처리

    while queue: #큐가 빌때까지
        v = queue.popleft() #FIFO
        print(v, end ='') 

        for i in graph[v]: #해당 노드와 연결됐지만, 아직 방문하지 않은 노드를 queue에 넣고 방문처리
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

bfs(graph,1,visited)