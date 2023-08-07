from collections import deque
m, n = map(int, input().split()) # 가로 ,세로

box = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))
            visited[i][j] = 0 

dr = [0, 0, 1, -1]
dc = [1, -1, 0 ,0]

while queue:
    for _ in range(len(queue)): # 하루씩 확인해야하기에, 전날 익은것들만큼만 확인(level 별)
        i , j = queue.pop()

        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]

            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1 and box[nr][nc] == 0:
                box[nr][nc] = 1
                queue.appendleft((nr,nc))
                visited[nr][nc] = visited[i][j] + 1

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()

print(max([max(row) for row in visited]))