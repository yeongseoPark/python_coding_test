# https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())

graph = [list(map(int,input())) for i in range(n)]

visited = [[False] * n for i in range(n)]

def bfs(x,y):
    cnt = 0

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    queue = deque()

    if graph[x][y] == 1:
        queue.append((x,y))
        visited[x][y] = True
        cnt += 1

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 1 and visited[nx][ny] == False:
                        queue.append((nx,ny))
                        visited[nx][ny] = True
                        cnt += 1
    return cnt

li = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j]==False:
            li.append(bfs(i,j))

print(len(li))

for i in sorted(li):
    print(i)


