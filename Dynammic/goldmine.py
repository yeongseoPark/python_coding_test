# n*m 크기의 금광 
# 금광은 1*1 크기의 칸으로 나누어짐
# 각 칸은 특정한 크기의 금이 들어있음
# 채굴자는 첫 번째열부터 출발하여 금을 캐기 시작
# 맨 처음에는 첫번째 열의 어느 행에서든 출발 가능
# 이후 m번에 걸쳐서 매번 오른쪽 위/오른쪽/ 오른쪽 아래 3가지 중 하나의 위치로 이동해야 함
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기 출력하기

# 문제의 점화식 dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

for testcase in range(int(input())):
    # 금광정보
    n,m = map(int,input().split()) # n 세로 / m 가로
    array = list(map(int,input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
    # dp테이블에 초기 데이터를 담아서 점화식에 따라 dp 테이블 갱신
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m]) 
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1,m): # 가로로 두번째부터 끝까지 (array를 넣은 dp테이블을 그대로 사용)(첫번째 열은 점화식에서 사용하기 위해 건너뜀(j-1))
        for i in range(n): # 각 열
            # 왼쪽 위에서 오는 경우
            if i ==0: # 만약에 왼쪽 위가 없다면
                left_up = 0 
            else: # 왼쪽 위가 있는 경우
                left_up = dp[i-1][j-1] # 왼쪽위의 값 left_up에 저장
            
            # 왼쪽 아래에서 오는 경우(왼쪽 위에서 오는것과 마찬가지 논리)
            if i == n-1: 
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            # 왼쪽에서 오는경우, 여기는 리스트 범위 벗어나는지 체크할 필요 x
            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(left_up,left_down,left) 
            #왼쪽 위, 왼쪽 아래, 왼쪽 중 가장 큰 값 dp 테이블에 더함 
    
    result = 0
    for i in range(n): # 위의 과정을 거치며, dp테이블의 마지막 열에 최대 금 크기가 각각 저장돼 있으므로, 이중 제일 큰 것을 고르면 됨
        result = max(result,dp[i][m-1])
    
    print(result)
            
    