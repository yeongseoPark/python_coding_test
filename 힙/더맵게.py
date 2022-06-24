import heapq

def solution(scoville, K): # 효율성 시간초과
    
    heapq.heapify(scoville)
    
    cnt = 0
    
    while True:
        if min(scoville) >=  K:  # 모두 k이상인 경우 끝냄
            break
            # 여기서 min을 사용하지 않고, scoville[0] >= K 를하게되면 효율성 통과가능
            # min()함수 사용시 배열 전체를 탐색하면서 min값을 찾아서 시간이 많이 걸리는데,
            # heapq인(최소힙) scoville은 자연스럽게 최솟값이 맨 앞에 오므로 그냥[0]번 인덱스 값 꺼내오면 됨
        minest = heapq.heappop(scoville) # 제일 작은 
        second_min = heapq.heappop(scoville) # 두번째로 작은 
        heapq.heappush(scoville,minest+(2*second_min)) # 섞음 
        
        cnt += 1 # 섞는 횟수
        
        if len(scoville) < 2 and scoville[0] < K: # 모든 음식의 스코빌지수 K이상 만들수 없음
            return -1
        
    return cnt
