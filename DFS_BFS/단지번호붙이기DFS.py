n = int(input())

graph = [list(map(int,input())) for i in range(n)]

visited = [[False] * n for _ in range(n)]

def dfs(x,y):
    global cnt # 전역변수인 cnt값 가져다 씀, 함수안에 cnt가 있으면 재귀함수로 들어갈때마다 초기화

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    if graph[x][y] == 1:
        cnt += 1
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    dfs(nx,ny)
                    
cnt = 0

li = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(i,j) #dfs로 cnt값 증가시켜줌
            li.append(cnt) # 이를 리스트에 넣은 후
            cnt = 0  # 카운트값 초기화

print(len(li))

for i in sorted(li):
    print(i)