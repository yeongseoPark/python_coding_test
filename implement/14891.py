import sys
input = sys.stdin.readline

# 0 : 12시 방향, 2 : 오른쪽 맞물린, 6 : 왼쪽 맞물린
wheels = [
    [int(c) for c in input().rstrip()] for _ in range(4)
]

k = int(input())
rotates = [(map(int, input().split())) for _ in range(k)]

def rotate(direction, number):
    if direction == 1: # 시계방향회전
        last_to_first = wheels[number][-1]
        for i in range(7,0, -1):
            wheels[number][i] = wheels[number][i-1] 
        wheels[number][0] = last_to_first

    else:
        first_to_last = wheels[number][0]
        for i in range(7):
            wheels[number][i] = wheels[number][i+1] 
        wheels[number][-1] = first_to_last

def rotate_flow(direction, num):
    visited[num] = True

    # 먼저 왼쪽 톱니바퀴들을 확인하고 회전
    if num - 1 >= 0 and wheels[num-1][2] != wheels[num][6] and not visited[num-1]: 
        rotate_flow(1 if direction == -1 else -1, num - 1)

    # 먼저 오른쪽 톱니바퀴들을 확인하고 회전
    if num + 1 <= 3 and wheels[num+1][6] != wheels[num][2] and not visited[num+1]: 
        rotate_flow(1 if direction == -1 else -1, num + 1)

    # 다른 연결된 톱니바퀴들을 확인하고 회전한 후에 현재 톱니바퀴를 회전
    rotate(direction, num)

for num, direction in rotates:
    visited = [False] * 4

    rotate_flow(direction, num-1)

ans = 0
ans += wheels[0][0] 
ans += wheels[1][0] * 2
ans += wheels[2][0] * 4
ans += wheels[3][0] * 8

print(ans)


