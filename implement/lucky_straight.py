# 필살기 "럭키스트레이트" / 점수가 특정 조건 만족해야 사용 가능
# 현재 점수 n일때, 자릿수 기준으로 n을 반으로 나누어서, 왼쪽부분 각 자릿수 합과 오른쪽 부분의 각 자릿수 합 더한 값이 동일한 경우
# 현재 점수 n에서 럭키스트레이트 사용할 수 있는 상태인지 알려주는 프로그램 작성


# 1 내 풀이
n = int(input()) # 10<=n<=99999999 # n의 자릿수는 항상 짝수형태

strn = str(n) 
length   = len(strn)
standard = length//2 

first  = strn[:standard]
second = strn[standard:]

first_sum = 0
for i in first:
    first_sum += int(i)

second_sum = 0
for j in second:
    second_sum += int(j)

if first_sum == second_sum:
    print('LUCKY')
else:
    print('READY')


# 2 답안
n = input() #str로 받음
length = len(n) 
summary = 0

for i in range(length//2):
    summary += int(n[i]) # 필요할때만 int변환
    # 양쪽 더해서 비교 말고, 한쪽 더하고 - 거기서 한쪽 빼줘서 0이면 같게되는 것 이용

for j in range(length//2,length):
    summary -= int(n[j])

if summary == 0:
    print("LUCKY")
else:
    print("READY")