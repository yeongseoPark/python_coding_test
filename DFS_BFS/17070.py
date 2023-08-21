from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ways = 0
W = 0 # 가로
H = 1 # 세로
D = 2 # 대각

def dfs(x, y, shape):
    global ways
    
    if x == n-1 and y == n-1:
        ways += 1
        return
    
    if shape == W or shape == D:
        if y + 1 < n and board[x][y+1] == 0:
            dfs(x, y+1, W)
    
    if shape == H or shape == D:
        if x + 1 < n and board[x+1][y] == 0:
            dfs(x+1, y, H)
    
    if x+1 < n and y+1 <n :
        if board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
            dfs(x+1, y+1 , D)

dfs(0, 1, W)
print(ways)