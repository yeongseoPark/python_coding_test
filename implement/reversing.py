# https://www.acmicpc.net/problem/1439



s = input()

count0 = 0 # 전부 0으로 바뀌는 경우
count1 = 0 # 전부 1로 바뀌는 경우

if s[0] == '1': # 첫 원소가 1인 경우
    count0 += 1 # 0으로 바꿀 소요 1늘어남
else:
    count1 += 1  # 위와 반대

for i in range(len(s)-1):
    if s[i] != s[i+1]: #불연속(이전값과 다음값이 다른 경우에만 뒤집기 소요가 발생)
        if s[i+1] == '1': # 0 - 1 의 경우
            count0 += 1   # 0으로 바꿀 소요 하나 늘어남
        else:
            count1 += 1 # 반대

print(min(count0,count1))

