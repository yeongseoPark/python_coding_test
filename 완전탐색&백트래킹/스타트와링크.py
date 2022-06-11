# https://www.acmicpc.net/problem/14889

from itertools import combinations


n = int(input())

overall = [list(map(int,input().split())) for _ in range(n)] 


lists = list(combinations(range(n),n//2)) # 가능한 모든 팀 경우의 수  # 스타트팀

dif = [] # 차이 담을 배열 

 
for i in lists: # 스타트팀 모든 경우의 수 for문 돌려서 
    opposite = list(range(n)) # 각 경우의 수의 반대 팀만들기 위한 전체인원 리스트(링크팀)

    start = 0 
    link = 0
 
    pairs = list(combinations(i,2)) # 스타트팀의 짝
    
    for j in pairs:
        start += overall[j[0]][j[1]] + overall[j[1]][j[0]] # start 능력치에 더해줌
         
    for k in i:
        opposite.remove(k) # 링크팀 만들어줌

    opposite_pairs = list(combinations(opposite,2)) # start팀 능력치 구하는 것과 마찬가지의 과정 반복

    for h in opposite_pairs:
        link += overall[h[0]][h[1]] + overall[h[1]][h[0]]
    
    dif.append(abs(start-link)) # 두 팀간의 차이 리스트에 더해줌

print(min(dif))



# print(dif)

