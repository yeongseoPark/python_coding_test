# n*n의 정사각형
# 주어진 L,R,U,D에 따라 이동
# 시작좌표는 1,1
# 정사각형 벗어나는 움직임 무시됨
# 최종적으로 도착할 지점 좌표 출력

# 1
n = int(input())
x, y= 1, 1 # 상 하 x / 좌 우 y 
directions = input().split()

move_type = ["l","r","u","d"]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for direction in directions:
    for i in range(len(move_type)):
        if direction == move_type[i]:
            nx = x + dx[i] # move_type과 dx,dy인덱스값 맞춰놓아서 가능
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue # 범위 벗어날시 반영 x
        
    x,y = nx ,ny
print(x, y)


# 2 : 모든 경우의수 if elif로 나눠줌 
for i in directions:
    if i == "l":
        if y == 1:
            y += 1
        y -= 1
    elif i == "r":
        if y == n:
            y -= 1        
        y += 1

    elif i == "u":
        if x == 1:
            x += 1
        x -= 1
        
    elif i == "d":
        if x == n:
            x -= 1       
        x += 1

# print(f"{x} {y}")
    



