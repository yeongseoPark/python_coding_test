# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque # 양방향 큐인 deque 사용

def solution(priorities, location):
    answer = 1 #출력순서
 
    d = deque((v,i) for i, v in enumerate(priorities))
    # enumerate로 deque에 (우선순위, 인덱스) 저장

    while len(d):
        item = d.popleft() # (우선순위, 인덱스 나옴)
        if d and max(d)[0] > item[0]: 
            # deque가 텅비지 않았고, 현재 우선순위보다 높은 우선순위가 있다면
            d.append(item)
        else: # item이 출력될 차례라면
            if item[1] == location: # 만약 꺼낸 item의 인덱스값이 location이라면 끝냄
                break 
            answer += 1 #location의 인쇄순서 += 1

    return answer 

solution([2,1,3,2],2)