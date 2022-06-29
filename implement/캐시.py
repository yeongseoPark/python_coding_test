from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    lru = deque()
    # cities = deque(cities)
    time = 0
    while cities:
        a = cities.pop().lower()
        if len(lru) < cacheSize:
            if a not in lru:
                lru.append(a)
                time += 5
            elif a in lru:
                lru.remove(a)
                lru.append(a)
                time += 1
        else: # else를 안붙여줬더니.. cacheSize보다 작은 경우에도 밑의 코드를 실행해서 에러났음..
            # if - elif -else분기를 꼭해주자..
            if a in lru:
                time += 1
                lru.remove(a)
                lru.append(a)
            else: 
                lru.popleft()
                lru.append(a)
                time += 5
    return time