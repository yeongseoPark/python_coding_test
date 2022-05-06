# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations

def solution(nums):
    sums = list(combinations(nums,3))
    prime_list = []
    for i in sums:
        divider = [j for j in range(1,sum(i)+1) if sum(i)%j ==0]
        if len(divider) == 2:
            prime_list.append(sum(i))
    return len(prime_list)

    # 2. break문으로, 1과 자기자신 제외한 나눠지는 수 있는 경우 break걸기
    answers = 0
    for a in combinations(nums,3):
        cand = sum(a)
        for j in range(2,cand):
            if cand % j ==0: # 소수 아님
                break
            else:  
                answer += 1
    return answer

print(solution([1,2,7,6,4]))