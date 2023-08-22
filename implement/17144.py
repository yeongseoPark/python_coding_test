import sys
input = sys.stdin.readline
import copy

R, C, T = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(map(int, input().strip().split())))
circulator = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            circulator.append([i,j])

def diff():
    dust_pos = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 1:
                dust_pos.append([i,j,arr[i][j]])
                
    for r, c, amount in dust_pos:
        d = [(0,1), (0, -1), (1,0), (-1,0)]
        for i in d:
            nr = r + i[0]
            nc = c + i[1]
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] != -1:
                    arr[nr][nc] += amount // 5
                    arr[r][c]   -= amount // 5

def move():
    temp = copy.deepcopy(arr)
    
    # 위
    r1, c1 = circulator[0]
    arr[r1][1] = 0
    for i in range(2, C): # 아래
        arr[r1][i] = temp[r1][i-1]
    for i in range(r1-1, -1, -1): # 오른쪽
        arr[i][C-1] = temp[i+1][C-1]
    for i in range(C-2, -1, -1): #위
        arr[0][i] = temp[0][i+1]
    for i in range(1, r1): # 왼쪽
        arr[i][0] = temp[i-1][0]

    # lower
    r2, c2 = circulator[1]
    arr[r2][1] = 0
    for i in range(2, C): # 위
        arr[r2][i] = temp[r2][i-1]
    for i in range(r2+1, R): # 오른쪽 
        arr[i][C-1] = temp[i-1][C-1]
    for i in range(C-2, -1, -1): # 아래
        arr[R-1][i]  = temp[R-1][i+1]
    for i in range(R-2, r2, -1): # 왼쪽
        arr[i][0] = temp[i+1][0]
        
for _ in range(T):
    diff()
    move()
ans = 0
for i in range(R):
    ans += sum(arr[i])
print(ans+2)