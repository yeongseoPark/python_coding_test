n = int(input())
nums = list(map(int, input().split()))

dp1 = [0 for _ in range(n-1)] + [nums[-1]]

# 수를 제거하지 않는 경우의 dp 테이블
for j in range(len(nums)-2, -1, -1):
    dp1[j] = max(dp1[j+1] + nums[j], nums[j])


dp2 = [0 for _ in range(n-1)] + [nums[-1]]
# 수를 제거하는 경우의 dp 테이블
for j in range(len(nums)-2, -1, -1):
    dp2[j] = max(dp1[j+1], dp2[j+1] + nums[j])
    # dp1[j+1] : 현재 j번째 숫자를 제거한 경우, 
    # dp2[j+1] + nums[j] : j번째 숫자가 아닌, 그 이전의 숫자 무언가를 제거한 경우
    # 이 둘중 max 값이 dp2에 들어감

print(max(max(dp1), max(dp2)))
