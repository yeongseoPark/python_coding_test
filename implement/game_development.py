# # n * m 직사각형 안 어딘가 위치한 캐릭터
# # 캐릭터는 동서남북 중 한 곳 바라봄 
# # 각 칸은 (a,b)로 나타내는데, a는 위에서부터 0 1 2 3... / b는 왼쪽서부터 0 1 2 3..
# # 1. 현재 방향 기준 왼쪽 방향(반시계 90도)도 부터 차례대로 갈 곳 정함
# # 2. 캐릭터 왼쪽 방향에 아직 가보지 않은 칸 존재한다면, 왼쪽으로 회전한 다음 왼쪽으로 한칸 전진
# # 2. 왼쪽 방향에 가보지 않은 칸 없다면 왼쪽 방향을 회전만 수행하고 1단계로 돌아간다.
# # 네방향 모두 가보았거나, 바다로 돼 있는 칸인 경우에, 바라보는 방향 유지한 채 한 칸 뒤로 간 이후 1단계로 돌아감
# # ㄴ 이때 뒤로 가려는데 바다이면 움직임을 멈춘다.

# # 매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램 만들기


# n, m  = map(int,input().split()) 

# # 방문한 위치 저장하려는 맵 생성(0으로 초기화 된 상태)
# d = [[0]*m for _ in range(n)]

# #캐릭터 현재 좌표와 방향 입력받기
# x,y,direction = map(int,input().split())
# d[x][y] = 1 #현재 좌표 방문 처리

# # 전체 지도 정의
# array = []
# for i in range(n):
# #     array.append(list(map(int,input().split())))

# # # 북 동 남 서. 순 방향 정의
# # dx = [-1,0,1,0] 
# # dy = [0,1,0,-1]

# # def turn_left():
# #     global direction # 밖에서 선언된 direction 변수 사용
# #     direction -= 1  # 왼쪽으로 회전
# #     if direction == -1: # 북(0)에서 회전하려면 서(3)으로 이동
# #         direction = 3

# # count = 1
# # turn_time = 0 
# # while True:
# #     turn_left()
# #     nx = x + dx[direction]
# #     ny = y + dy[direction]
    
# #     #회전한 이후 정면 칸이 가보지 않았고 육지이면
# #     if d[nx][ny] == 0 and array[nx][ny] == 0:
# #         d[nx][ny] = 1
# #         x = nx
# #         y = ny
# #         count += 1
# #         turn_time = 0 
# #         continue # 밑의 코드 건너뜀

# #     # 회전한 이후 정면 칸이 가봤거나 바다인 경우
# #     else:
# #         turn_time += 1 # 왼쪽으로 한번 더 돌음
    
# #     if turn_time == 4:
# #         nx = x - dx[direction]
# #         ny = y - dy[direction]
# #         #뒤로 갈 수 있으면 가보기
# #         if array[nx][ny] == 0:
# #             x ,y = nx,ny
# #         else:
# #             break # 뒤가 바다로 막혀있어서 더 이상 갈 수 없음
# #         turn_time = 0 # 뒤로 가기 성공한 경우 turn_time 초기화

# # print(count)



n,m = map(int,input().split())

a, b , d = map(int,input().split()) # 좌표, 방향

dy = [-1,0,1,0]
dx = [0,1,0,-1] # 북동남서

mapp = [list(map(int, input().split())) for j in range(n)]


visited = 1
end = True 

while end:
    if d == 0: # 각 방향에 맞는 회전순서
        direction = [3,2,1,0] 
    elif d==3:
        direction = [2,1,0,3]
    elif d==2:
        direction = [1,0,3,2]
    else:
        direction = [0,3,2,1]

    mapp[a][b] = 1

    rotate_cnt = 0

    for i in direction:
        if a+dy[i] < 0 or a+dy[i] > n-1 or b+dx[i] <0 or b+dx[i] > m-1:
            # 돌아서 한칸 갔는데 지도 벗어나면
            rotate_cnt += 1 # 돈 횟수 += 1하고 다음i로 건너감(continue)
            if rotate_cnt == 4: # 네번돌았으면
                if mapp[a-1][b] == 1 or a-1 < 0 or a-1 > n:  
                    # 뒤로 한칸가려는데 못가면
                    end = False # while문 끝내야한다
                    break # for문탈출 함
                else: #뒤로 갈 수 있으면
                    a -= 1 # 뒤로가고
                    break # for문 끝냄
            continue
 
        elif mapp[a+dy[i]][b+dx[i]] == 0: # 돌아서 한칸 갔는데 0이면
            a = a+ dy[i] # a바꿔주고
            b = b+ dx[i] # b 바꿔주고
            d = i # 방향도 바꿔준다
            visited += 1 # 방문횟수 += 1
            break # for문 탈출

        else: # 돌아서 한칸 갔는데 1이면 
            rotate_cnt += 1 # 돈 횟수 += 1
            if rotate_cnt == 4:
                if mapp[a-1][b] == 1  or a-1 < 0 or a-1 > n:
                    end = False
                    break
                else:
                    a -= 1

print(visited)


















