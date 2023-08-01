n,m,x,y,k = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

move = list(map(int, input().split()))

# 위 뒤 오 왼 앞 바닥
dice = [0,0,0,0,0,0]

def turn(dir):
    a,b,c,d,e,f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c
    elif dir == 2: # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d
    elif dir == 3: # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e

# 동 서 북 남
dx = [0,0,-1,1]
dy = [1, -1, 0, 0]

nx, ny = x, y
for i in move:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    
    turn(i)
    if box[nx][ny] == 0:
        box[nx][ny] = dice[-1]
    else:
        dice[-1] = box[nx][ny]
        box[nx][ny] = 0
    
    print(dice[0])