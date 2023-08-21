import copy

n,m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

cctv = []
for i in range(n):
    for j in range(m):
        if b[i][j] != 0 and b[i][j] != 6:
            cctv.append((b[i][j], i, j))

# 북 동 남 서 
dr = [-1, 0, 1, 0]
dc = [0, 1, 0 , -1]

# cctv 방향 정보
mode = [
    [],
    [[0], [1], [2], [3]], # 1번
    [[0,2], [1,3]],       # 2번  : 남북 or 동서
    [[0,1], [1,2], [2,3], [0,3]], # 3번 : 직각 방향 다
    [[0,1,2], [0,1,3], [1,2,3], [0,2,3]], # 4번 : 3방향 다
    [[0,1,2,3]] # 5번
]

def fill(b, mode, r, c): # 감시
    for i in mode:
        nr = r
        nc = c
        while True:
            nr += dr[i]
            nc += dc[i]
            
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                break
            
            # 벽을 만나면 중단
            if b[nr][nc] == 6:
                break
            
            # 감시가 가능 ~-> -1로 변경
            elif b[nr][nc] == 0:
                b[nr][nc] = -1

def dfs(depth, b):
    global min_val
    # cctv 전체를 탐색 완료
    if depth == len(cctv):
        count = 0
        for i in b:
            count += i.count(0)
        min_val = min(min_val, count)
        return
    
    temp = copy.deepcopy(b)
    cctv_num, r, c = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, r,c)
        dfs(depth+1, temp)
        temp = copy.deepcopy(b)

min_val = int(1e9)
dfs(0, b)
print(min_val)