from collections import deque

n = int(input())
lands = [list(map(int, input().split())) for _ in range(n)]

# 1부터 최대 높이까지 안전영역 조사해야 하므로 최대 높이 확인
max_height = -1
for row in lands:
    for land in row:
        max_height = max(max_height, land)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# limit 초과 높이를 갖는 안전 영역을 탐색
def bfs(r, c, limit):
    q = deque()

    q.append((r,c))
    visited[r][c] = True

    while q:
        row , col = q.popleft()

        for k in range(4):
            nr = row + dr[k]
            nc = col + dc[k]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and lands[nr][nc] > limit:
                visited[nr][nc] = True
                q.append((nr, nc))

max_cnt = 0 # 최대 안전 영역 개수
for limit in range( max_height+1): # limit가 0인경우, 그니까 비가 안오는 경우도 테스트케이스로 고려해야 함
    visited = [[0] * n for _ in range(n)]
    cnt = 0 # 특정 높이에서 안전 영역 개수
    for i in range(n):
        for j in range(n):
            if lands[i][j] > limit and not visited[i][j]:
                bfs(i,j, limit)
                cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)