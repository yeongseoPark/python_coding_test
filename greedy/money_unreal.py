# n개의 동전
# n개의 동전으로 만들 수 없는 양의 정수 금액 중 최솟값 구하기
from itertools import combinations # 조합(콤비네이션) 구하는 파이썬 라이브러리 itertools

n = int(input()) # 1~1000
penny = list(map(int,input().split()))

# 1개~5개 더하는 모든 경우의 수 고려하는 법? : 조합 사용
all_results = []
for i in range(1,len(penny)+1): 
    i_combi = list(combinations(penny,i)) # 5c1 ~ 5c5
    for j in i_combi:
        all_results.append(sum(j))

#1~전체 결과중 최댓값에서,all_results 중간에 비어있는 첫번째 값이 최소값임
for i in range(1,max(all_results)):
    if i not in all_results:
        print(i)
        break


# 책 풀이
penny.sort() # 화폐 단위 기준으로 오름차순 정렬

target = 1
for x in penny: #1부터 차례대로 target 만들 수 있는지 확인

    if target < x:
        break
    target += x # target을 만들 수 있다면 업데이트

print(target)