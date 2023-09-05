import heapq
from collections import defaultdict

for _ in range(int(input())):
    min_h = []
    max_h = []
    k = int(input())
    
    # 처음에는 아무값도 없으므로 모두 삭제된 것으로 간주
    # 각 노드의 아이디(순번)에 따라 그 노드가 삭제되었는지 아닌지를 저장
    deleted = [1] * k
    
    for i in range(k):  # 입력 데이터
        v, n = input().split()  # 연산, 숫자
        n = int(n)

        if v == "I":
            heapq.heappush(min_h, (n, i))
            heapq.heappush(max_h, (-n, i))
            deleted[i] = False

        elif v == "D":
            if n == 1:  # 최댓값 삭제
                
                # 삭제되지 않은 값 찾기
                # 삭제된 값은 힙에서 제거
                while max_h and deleted[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    deleted[max_h[0][1]] = True
                    heapq.heappop(max_h)

            elif n == -1:  # 최솟값 삭제
                while min_h and deleted[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    deleted[min_h[0][1]] = True
                    heapq.heappop(min_h)

    # 연산이 끝난 후 삭제된 값들 제거
    while min_h and deleted[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and deleted[max_h[0][1]]:
        heapq.heappop(max_h)

    
    if min_h and max_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print("EMPTY")
