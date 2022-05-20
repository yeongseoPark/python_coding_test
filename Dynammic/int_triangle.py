# https://www.acmicpc.net/problem/1932
# 정수 삼각형의 맨 위층부터 시작해서, 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
# 이제까지 선택된 순의 합이 최대가 되는 경로를 구하는 프로그램 작성
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택 가능

n = int(input()) # 1<=n<=500

# dp[h][w] = triangle[h][w] + max(triangle[h-1][w-1], triangle[h-1][w]))
# 모든 위치 기준으로 이전 위치로 가능한 두가지 위치(왼쪽 위, 그냥 위) 중 더 큰 합 가지는 경우 선택

dp = []

for _ in range(n):
    dp.append(list(map(int,input().split())))

# # dp테이블에 초기 데이터 담고, 점화식에 따라 dp테이블 갱신 -> 이전 금광 문제와 유사

for i in range(1,n):
     for j in range(i+1):
         # 왼쪽 위 
        if j == 0:
             up_left = 0
        else:
            up_left = dp[i-1][j-1]
        
        # 바로 위
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]))


# 내 풀이
triangle = []
for i in range(n):
    triangle.append(list(map(int,input().split())))


dp = []
dp.append(triangle[0])
for i in range(1,n): # 세로로 두번째 부터 끝까지
    dp.append(triangle[i]) # 이 코드 없으면 58번째 라인에서
    for j in range(i+1): # 가로 길이 
        if j == 0:
            left = 0
        else:
            left = dp[i-1][j-1]
        
        if j == i:
            right = 0
        else:
            right = dp[i-1][j]
        
        dp[i][j] = triangle[i][j] + max(left,right) # 여기서 빈리스트(dp[i])에 j번째 인덱스에 값 넣으려하면 index out of range 남
        # 이렇게 풀기보단 그냥 dp테이블에 처음부터 데이터 입력받아서 담고, 점화식 따라 갱신하는 방법이 나은듯

count = 0
for i in range(n):
    count = max(dp[n-1][i],count)

print(count)
