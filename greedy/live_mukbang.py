# https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq # 우선순위 큐 https://m.blog.naver.com/jjys9047/222075711112

def solution(food_times, k): #음식먹는데 필요한 시간이 음식 번호 순서로 배열 / 방송이 중단된 시간
    answer = -1 # answer 못 구할 경우: -1

    # 시간이 작은 순서대로 빼기 위해, 최소값 우선순위로 하는 우선순위 큐 사용
    q = []
    for i in range(len(food_times)): 
        heapq.heappush(q,(food_times[i], i+1)) # 모든 음식을 (음식 시간, 음식 번호)의 형태로 우선순위 큐에 삽입

    previous  = 0  # 직전에 다 먹은 음식의 시간
    length    = len(food_times) # 남은 음식 개수

    while q: 
        # 가장 적은 섭취시간 - 전 음식의 섭취시간 곱하기 음식개수 -> 음식 하나 다먹는데 걸리는 시간
        # 전 음식을 빼주는 이유는, 이전 음식을 먹을때에도 현재 음식을 먹기 때문
        diff = (q[0][0] - previous) * length 
        # 음식하나 다 먹는 사이클 돌려도 그 시간이 k보다 적을때
        if diff <= k:
            k -= diff # 음식하나 다 먹는데 걸리는 소요시간 k에서 빼줌
            length -= 1 # 음식 다먹었으니 제외
            previous, _ = heapq.heappop(q) #음식 리스트에서 제외, previous에 이 음식 섭취시간 기록
        else: # 더이상 사이클 돌릴 수 없음
            idx = k % length # 남은 시간 % 남은 음식 종류 수 => 남은 k초동안 남은 음식 먹으면 마지막은 몇번째?
            q.sort(key=lambda x:x[1]) #큐를 음식 번호 순으로 정렬 

            answer = q[idx][1] 
            break
    return answer
    

