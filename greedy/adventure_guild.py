# n명의 모험가 대상 '공포도'측정
# 공포도 높으면 상황 대처 능력 떨어짐
# 공포도 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 떠날 수 있음
# 최대 몇개의 모험가 그룹?

# n명의 모험가에 대한 정보 주어질때, 여행 떠날 수 있는 그룹 수의 최댓값 구하기
# 모든 모험가를 특정한 그룹에 넣을 필요는 없음(남아도 됨)

n = int(input()) # 1<=n<=100000

fear = list(map(int,input().split()))# 각 모험가 공포도의 값 n 이하의 자연수로 주어짐

fear.sort() # 오름차순 정렬

group_number = 0  # 그룹의 개수
group_size = 0    # 그룹의 크기

for i in fear:
    group_size += 1 # 그룹의 크기가 현재 공포도보다 낮다면 크기 하나 늘림
    if group_size >= i: # 그룹크기>현재 공포도 일 시 
        group_number += 1 #그룹 결성
        group_size = 0

print(group_number)
        

# count = 0
# number = len(fear)
# for i in range(1,n):
#     number -= fear[n-i]
#     count += 1
#     if number < 0 :
#         break
    
# print(count)
