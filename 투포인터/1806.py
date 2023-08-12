n, s = map(int, input().split())
seq = list(map(int, input().split()))
start = 0
end   = 0
temp_sum = seq[0]
min_length = 100001

while True:
    if end < len(seq)-1:
        # 부분합이 S미만인 경우
        if temp_sum < s:
            end += 1 # 오른쪽으로 한칸 이동
            temp_sum += seq[end] # 부분합에 한칸 이동한 값을 더함
        # 부분합이 S 이상인 경우
        elif temp_sum >= s:
            min_length = min(min_length, end - start + 1) # 현재 부분수열의 길이와 현재까지의 최소 길이 중 작은 값
            temp_sum -= seq[start] # 부분합에서 가장 왼쪽의 값을 뺌
            start += 1 # 가장 왼쪽을 오른쪽으로 한 칸 이동
    else: # 오른쪽은 끝에 다다랐으니 왼쪽을 줄여가다가 끝내면 됨
        while temp_sum >= s:
            min_length = min(min_length, end - start + 1)
            temp_sum -= seq[start]
            start += 1
        break

print(0 if min_length == 100001 else min_length)