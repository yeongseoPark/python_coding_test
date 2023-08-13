n = int(input())
m = int(input())
broken = set()
if m != 0:
    broken = set(map(int, input().split()))

# 현재 채널(100)에서 바로 가는 경우
ans = abs(n - 100)

# 모든 경우의 수를 탐색
for channel in range(9999101): 
    for j in range(len(str(channel))):
        if int(str(channel)[j]) in broken: # 입력이 불가능함
            break
        elif j == len(str(channel)) - 1: # 채널이 입력이 가능함
            ans = min(ans, abs(channel - n) + len(str(channel)))
print(ans)
