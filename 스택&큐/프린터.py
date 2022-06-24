# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque # 양방향 큐인 deque 사용 

def solution(priorities, location): # 답 보고 품
    answer = 1 #출력순서
 
    d = deque((v,i) for i, v in enumerate(priorities)) # 밑의 코드에서는 k를 하나씩늘려가며 인덱스를 넣어줬는데
    # 여기서는 enumerate사용하여 훨씬 깔끔해짐
    # enumerate로 deque에 (우선순위, 인덱스) 저장

    d= ([ (1, 1), (3, 2), (2, 3), (2, 0)])
    
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



def solution(priorities, location): # 스스로 품
    
    d = deque() 
    
    k = 0
    for i in priorities:
        d.append([i,k]) # deque에 (우선순위, 인덱스) 담음 -> .index()로 인덱스 담으면, 중복되는 값들 있을시 제대로 동작하지 않음
        k += 1
    
    count = 0 # 인쇄되는 번째수
    
    while d:        
        a = d.popleft()
        
        if len(d) == 0: # popleft()한것이 d의 마지막 하나 남은 값이라면 밑의 if문에서 에러나므로
            return len(priorities)  # location에 해당하는애가 마지막에 인쇄되므로 그에 맞게 리턴
        
        if a[0] >= max(p[0] for p in d): # 만약에 맨 앞의 값보다 우선순위 높은 값이 뒤에 없다면
            count += 1   # 인쇄 번째수 += 1
            if a[1] == location: # 만약 이경우 location과 a의 index값 같다면
                 return count # 답 리터
        else:
            d.append(a) # 뒤로 다시 보냄
     
    return count
            

solution([2,1,3,2],2)