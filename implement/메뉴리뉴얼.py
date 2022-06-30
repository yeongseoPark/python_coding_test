from itertools import combinations
from collections import Counter

def solution(orders, course): # 접근방법은 맞았으나 구현을 못해서 답보고 품
    answer = []
    for i in course: #코스 메뉴 수들에 따라 반복문돌림
        combis = [] 
        for j in orders: # 고객의 주문들
            for k in list(combinations(j,i)): # 메뉴수만큼 조합 만들어서 
                combis.append("".join(sorted(k))) # combis에 넣음
        counter = Counter(combis)  # 특정조합 : 횟수 => AD : 3 처럼
        if len(counter) != 0 and max(counter.values()) != 1: 
            # counter가 비었고(아예 해당하는 경우가 없고), 최소 두명이상이 주문하지 않은 경우 제외
            for f in counter: # counter의 키값들 중
                if counter[f] == max(counter.values()): 
                    answer.append(f)
        
    return answer

   

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])