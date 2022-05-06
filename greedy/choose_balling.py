# 두 사람이 서로 무게가 다른 볼링공 고르려고 함
# 볼링공은 n개 / 각 볼링공엔 무게가 적혀있음 / 볼링공 번호는 1번부터 순서대로 부여됨
# 같은 무게의 공 여러개 있어도, 서로 다른 공
# 공 무게는 1~m 까지 자연수로 존재

n, m = map(int,input().split()) # 1<=n<=1000 , 1<=m<=10
k = list(map(int,input().split())) # 1<=k<=m # 볼링공의 무게 k개

from itertools import combinations

all_results = list(combinations(k,2)) # 모든 조합구하고 -> 거기서 무게 같은 경우 빼주면 됨

remove_list = []
for i in range(len(all_results)): 
    if all_results[i][0] == all_results[i][1]: #그냥 여기서 바로 인덱스 값으로 del해주면,
        # 리스트가 줄어들며 index out range 남
        remove_list.append(all_results[i])

for j in remove_list:
    all_results.remove(j)

print(len(all_results))


# 책 풀이 : a가 특정한 무게 골랐을 때, b가 이어서 볼링공 선택하는 경우 차례대로 계산
array = [0] * 11 # 1부터 10까지의 무게 담을 수 있는 리스트 (인덱스 값으로 구분, 0은비워둔다)
for x in k:
    array[x] += 1  # 볼링공의 무게에 해당하는 리스트 인덱스의 값에 += 1

result = 0 # 가능한 경우의 수 
for i in range(1,m+1): # 1부터 m(가능한 무게의 수)
    n -= array[i] # 특정 무게에 해당하는 볼링공 고르면, 똑같은 무게를 또 고를 수 없음
    result += array[i] * n # 특정 무게 볼링공 고르는 경우의 수 * 나머지 중 하나 고르는 경우의 수

print(result)

