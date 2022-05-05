#n * m 크기의 미로
#미로에 괴물이 있어서 피해서 탈출해야 함
#동빈이는 (1,1)에 있고 출구는(n.m)에 있음
#괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시됨 , 시작칸과 마지막칸은 항상 1 
#동빈이가 탈출하기 위해 움직여야 하는 최소 칸수

from collections import deque

n,m = map(int,input().split())

maze = [] #0혹은1의 정수 리스트
for i in range(n):
    maze.append(list(map(int,input())))

dx = [-1,1,0,0] # 상 하 좌 우 
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4): #상하좌우 범위 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0  or nx >= n or ny >= m: # 범위 벗어남
                continue

            if maze[nx][ny] == 0: # 괴물 만남
                continue

            if maze[nx][ny] == 1: # 갈 수 있는 길 
                maze[nx][ny] = maze[x][y] + 1 # 이전 노드 값(길의 한 칸 전) + 1
                queue.append((nx,ny))

    return maze[n-1][m-1] # 가장 오른쪽 아래의 값(36번 줄에서 + 된 값)을 리턴함.

print(bfs(0,0))











