def dfs(graph, v , visited): # dfs메서드를 정의함
    visited[v] = True # 현재 노드를 방문처리 함
    print(v, end= ' ') # 방문순서
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i ,visited) #recursion 
            # visited[i]가 모두 true면 none을 리턴함
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

visited = [False] * 9
dfs(graph,1,visited)