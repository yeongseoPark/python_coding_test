n, m = map(int, input().split())
r, c, direction = map(int, input().split())

# 북 동 남 서 (시계 방향)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

places = [list(map(int, input().split())) for _ in range(n)]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0
places[r][c] = 2

while True:
    turn_left()
    nr = r + dr[direction]
    nc = c + dc[direction]

    if places[nr][nc] == 0: # 아직 청소x
        places[nr][nc] = 2 # 청소함
        r, c = nr, nc
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4: # 후진 필요
        nr = r - dr[direction] # 한칸 전으로 가면됨
        nc = c - dc[direction]
        if places[nr][nc] == 1:
            break
        else:
            r, c = nr, nc
        turn_time = 0

print(cnt)
