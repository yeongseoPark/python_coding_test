from collections import deque

m , n = map(int, input().split())
arr = [[int(i) for i in input().rstrip()] for _ in range(n)]

visited = [[0] * m for _ in range(n)]
q = deque()
q.append((0,0, 0))
visited[0][0] = True

while q:
    r, c, cnt = q.popleft()
    
    if r == n-1 and c == m-1:
        print(cnt)
        break
    
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if not visited[nr][nc]:
                if arr[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc, cnt + 1))
                
                else:
                    visited[nr][nc] = True
                    q.appendleft((nr,nc,cnt))