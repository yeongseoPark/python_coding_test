password = input().rstrip()

dp = [0] * (len(password) + 1)
dp[0] = 1
dp[1] = 1

if password[0] == '0':  
    print(0)
    exit()

for i in range(2, len(password) + 1): 
    if password[i-1] > '0':
        dp[i] = dp[i-1]
    
    two_digit = int(password[i-2:i])  # 두 자리 숫자로 변환
    if 10 <= two_digit <= 26:  # 유효한 두 자리 숫자인지 확인
        dp[i] += dp[i-2]

    dp[i] %= 1000000  # 각 단계에서 실시해서 오버플로 방지

print(dp[-1])
