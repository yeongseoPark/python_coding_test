from collections import deque

R, C = map(int, input().split())
board = [[i for i in input().rstrip()] for _ in range(R)]

def bfs(start_r, start_c):
    q = deque()
    q.append((0, start_r, start_c)) # 거리, 행 , 열
    visited = [[0] * C for _ in range(R)]
    visited[start_r][start_c] = True
    
    max_val = -1
    
    while q:
        dist, r, c = q.popleft()
        
        max_val = max(max_val, dist)
        
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and board[nr][nc] == "L":
                q.append((dist + 1, nr ,nc))
                visited[nr][nc] = True
    
    return max_val

ans = -1
for i in range(R):
    for j in range(C):
        if board[i][j] == "L":
            ans = max(ans, bfs(i,j))

print(ans) 