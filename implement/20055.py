from collections import deque

N, k = map(int, input().split())

q = deque(list(map(int, input().split())))
robots = deque([0 for _ in range(2*N)])

def move_robots(robots):
    for i in range(N, -1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and q[i+1] >= 1:
            robots[i] = 0
            robots[i+1] = 1
            q[i+1] -= 1
    
    robots[N-1] = 0 # 로봇이 떨어집니다

def rotate(q, robots):
    q.rotate(1) # deque의 .roate()메서드
    robots.rotate(1)
    robots[N-1] = 0 # 떨어져야 함

def can_quit(q, k):
    cnt = 0 
    for i in range(len(q)):
        if q[i] == 0:
            cnt += 1
            if cnt >= k:
                return True
    
    return False

circle = 0
while True:
    circle += 1
    rotate(q, robots) # 벨트와 로봇이 회전
    move_robots(robots) # 로봇들도 한칸씩 이동(가능하면)
    
    # 올리는 위치 내구도 0 아니면 로봇 올림
    if q[0] > 0 and robots[0] == 0:
        robots[0] = 1
        q[0] -= 1
    
    if can_quit(q, k):
        print(circle)
        break