from collections import deque

def is_valid(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

for _ in range(int(input())):
    n = int(input()) # n*n 체스판
    cur_r, cur_c = map(int, input().split())
    goal_r, goal_c = map(int, input().split())
    
    if cur_r == goal_r and cur_c == goal_c:
        print(0)
        continue
    
    visited = [[0] * n for i in range(n)]
    visited[cur_r][cur_c] = 1
    
    q= deque()
    q.append((cur_r,cur_c))
    
    while q:
        r, c = q.popleft()
        
        if r==goal_r and c == goal_c:
            print(visited[r][c] - 1)
            break
        
        if is_valid(r-2, c-1, n) and not visited[r-2][c-1]:
            visited[r-2][c-1] = visited[r][c] + 1
            q.append((r-2,c-1))
        
        if is_valid(r-1, c-2, n) and not visited[r-1][c-2]:
            visited[r-1][c-2] = visited[r][c] + 1
            q.append((r-1,c-2))
            
        if is_valid(r-2, c+1, n) and not visited[r-2][c+1]:
            visited[r-2][c+1] = visited[r][c] + 1
            q.append((r-2,c+1))
            
        if is_valid(r-1, c+2, n) and not visited[r-1][c+2]:
            visited[r-1][c+2] = visited[r][c] + 1
            q.append((r-1,c+2))
        
        if is_valid(r+1, c-2, n) and not visited[r+1][c-2]:
            visited[r+1][c-2] = visited[r][c] + 1
            q.append((r+1,c-2)) 
        
        if is_valid(r+2, c-1, n) and not visited[r+2][c-1]:
            visited[r+2][c-1] = visited[r][c] + 1
            q.append((r+2,c-1))
        
        if is_valid(r+2, c+1, n) and not visited[r+2][c+1]:
            visited[r+2][c+1] = visited[r][c] + 1
            q.append((r+2,c+1))
        
        if is_valid(r+1, c+2, n) and not visited[r+1][c+2]:
            visited[r+1][c+2] = visited[r][c] + 1
            q.append((r+1,c+2))               