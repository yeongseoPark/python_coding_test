# 연구소 크기는 n*m 직사각형
# 각 직사각형은 1*1 정사각형으로 채워짐
# 빈칸 과 벽. 벽은 칸 하나 가득 차지
# 일부 칸은 바이러스 존재. 이 바이러스는 상하좌우 인접한 빈칸으로 모두 퍼져나갈 수 있음
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 합니다
# 0은 빈칸 / 1은 벽 / 2는 바이러스 
# 벽 세운 이후, 남은 빈칸에는 바이러스가 퍼져나감

# 안전 영역(벽 3개 세운 뒤 바이러스가 퍼질 수 없는 곳)의 최댓값은?? #벽은 꼭 3개 세워야 함

n,m = map(int,input().split()) #세로 n / 가로 m

data = [] # 초기 맵 리스트
for i in range(n):
    data.append(list(map(int,input().split()))) # 빈칸 갯수는 세개 이상

temp = [[0] * m for _ in range(n)] # 벽 설치한 뒤의 맵리스트

# 4가지 이동 방향
dx = [-1,0,1,0] # 상 우 하 좌 (시계 방향)
dy = [0,1,0,-1]

result = 0

# DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하 , 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx>= 0 and ny >= 0 and nx <= m and ny <= n:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] =2 
                virus(nx,ny)

# 현재 맵에서 안전영역의 크기 계산
def get_score():
    score = 0 
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS를 활용해 벽을 세우면서, 매번 안전영역의 크기를 계산해보자 

def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3: #왜 갑자기 설치함? -> 밑에서 빈공간에 설치하네(65~), 재귀사용해서
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j] # 왜 벽 설치뒤 맵이랑 초기맵이랑 동기화함? 벽설치 안했자나
        # 각 바이러스 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        # 안전영역에 울타리 설치
        result = max(result,get_score())
        return 
    # 빈 공간에 울타리 설치
    for i in range(n): # data[0][0]빈칸이면, 벽설치하고 ,카운트 늘리고, coutn=1인상태로 dfs(1)하면, 쭉쭉내려와서 67번줄에서 갈데가 없어지지 않나?
        for j in range(m):
            if data[i][j] == 0: # 빈칸이야
                data[i][j] = 1  # 벽설치해
                count += 1      # 벽설치횟수 + 1
                dfs(count)      # 이 상황에서 벽 설치 한번 더 
                data[i][j] = 0  #아...마... 계속 설치하고 지우고 하는거같은데....
                count -= 1

dfs(0)
print(result)



# 이때 안전 영역을 기록하자

