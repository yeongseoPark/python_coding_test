# def solution(citations): #12.5점
#     citations.sort(reverse=True)
#     for i in citations:
#         cnt = 0
#         for j in citations:
#             if j>= i:
#                 cnt += 1
#         if cnt >= i:
#             return i
    
def solution(citations):
    citations.sort(reverse=True)
    for i in range(max(citations),-1,-1): # 인용횟수 가장 많은 것~ 0
        cnt = 0
        for j in citations:
            if j>= i:
                cnt += 1
        if cnt >= i:
            return i # 만약에 h인덱스 조건 통과하면 바로 리턴하고 끝냄

solution([3,6,0,1,5])