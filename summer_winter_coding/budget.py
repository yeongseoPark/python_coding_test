# https://programmers.co.kr/learn/courses/30/lessons/12982
# from itertools import combinations

def solution(d, budget):   
    d.sort()
    count = 0
    for i in d:
        budget -= i
        if budget < 0: # 예산 마이너스 돼서 더이상 부서에게 예산 줄 수 없을때
            return count
        count  += 1
        if budget == 0: # 예산이 부서별에 맞게 딱 맞아 떨어지는 경우
            return count 
    if budget > 0:  # 모든 부서에 예산을 할당해도 남는 경우 -> 생각 못함.
        return len(d) 

    # # 2 테케에 걸림 : 딱 0이되는 경우에 대해 고려해주지 않았음 
    # d.sort()
    # count = 0
    # for i in d:
    #     budget -= i
    #     if budget < 0:  
    #         return count
    #     count  += 1
    


    # 1. 시간초과
#     lst = []
#     for i in range(1,len(d)+1):
#         combi = list(combinations(d,i))
#         for j in combi:
#             lst.append([j,sum(j)])

#     appropriate = []
#     for i in lst:
#         if i[1] <= budget:
#             appropriate.append(len(i[0]))
#     return max(appropriate)



# print(solution([1,3,2,5,4],9))


