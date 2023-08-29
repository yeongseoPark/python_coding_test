n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * (n-1) for _ in range(21)]
# dp[i][j] : j번째에서 i 값되는 등식 개수

# 첫번째에서 nums[0] 값은 무조건 됨
dp[nums[0]][0] = 1


for col in range(1, n-1): # 전체 열 순서로 탐색
    for num in range(21): # 각 행에서  
        if dp[num][col - 1] != 0: # 만약 전 열에서 행 값(0~20 사이 값)이 된다면 
            if num + nums[col] <= 20: # 전 값에 지금 숫자 값을 더한게 범위 안이라면
                dp[num+nums[col]][col] += dp[num][col-1] # 그 전 값에 가능했던 등식의 수를 (전 값 + 지금 숫자 값)에 기록해줌
            
            if num - nums[col] >= 0:
                dp[num-nums[col]][col] += dp[num][col-1]



print(dp[nums[-1]][n-2])