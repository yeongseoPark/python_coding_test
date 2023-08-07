from itertools import combinations
from collections import deque
import copy

"""
최대 8*8이기에
64C3 = 41664 -> 가능한 벽 가짓수

BFS 탐색은 O(64)

둘이 곱해봐야 41664 * 64 이므로 모든 경우의 수에대해 탐색해도 시간초과 안남
"""

n, m = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]
# 0 빈칸 / 1 벽 / 2 바이러스

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 바이러스를 bfs로 퍼트림 
def bfs(i,j):
    q = deque()

    q.append((i,j))

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < n and 0 <= nc < m and box_copy[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                box_copy[nr][nc] = 2
                q.append((nr,nc))

emptys = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            emptys.append((i,j))

max_free = -1
for tmp_walls in list(combinations(emptys, 3)):
    box_copy = copy.deepcopy(box) # 모든 벽 시나리오에 대해서 box를 변경하므로 box복사본을 두었다가 이를 사용

    for i,j in tmp_walls:
        box_copy[i][j] = 1

    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if box_copy[i][j] == 2:
                bfs(i, j)

    free = 0
    for i in range(n):
        for j in range(m):
            if box_copy[i][j] == 0:
                free += 1 

    max_free = max(free, max_free)

print(max_free)