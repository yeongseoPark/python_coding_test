from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(101)]
for _ in range(n+m):
    a, b = map(int,input().split())
    graph[a].append(b)

q = deque()
visited = [0] * 101
visited[1] = True
q.append((1,0)) # 현재 지점, 주사위 횟수

while q:
    cur, cost = q.popleft()
    
    if cur == 100:
        print(cost)
        break
    
    if graph[cur] != []:
        next = graph[cur][0]
        for i in range(1,7):
            if next + i <= 100 and not visited[next+i]:
                q.append((next+i, cost+1))
                visited[next+i] = True
        
        continue
        
    for i in range(1,7):
        if cur + i <= 100 and not visited[cur+i]:
            q.append((cur+i, cost+1))
            visited[cur+i] = True