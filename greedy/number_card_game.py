# 여러개 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한장 뽑는 게임
# N * M , N은 행 M은 열 개수

# 1.뽑고자 하는 카드 있는 행 선택
# 2.선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드 뽑아야 함
# 따라서 행 선택할 때 해당 행에서 가장 숫자 낮은 카드 뽑을 것 고려하여 
# 최종적으로 가장 높은 숫자의 카드 뽑게 전략 세워야 함

n,m = map(int,input().split())

#1
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
#이중 리스트

minest = []
for row in data:
    minest.append(min(row)) # 각row의 최솟값 리스트에 담음
print(max(minest))

#2
result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value) #1 처럼 리스트에 담고 거기서 최댓값 빼지 않고
    # 바로 이전 row최솟값과 비교하여 더 큰 쪽이 result에 남는 형식
print(result)