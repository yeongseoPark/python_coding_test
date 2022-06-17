from collections import deque

def solution(numbers, target): #bfs풀이
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0]) # numbers의 첫요소를 더한경우, 그것의 인덱스
    queue.append([-1*numbers[0],0]) # numbers의 첫요소를 뺀경우, 그것의 인덱스
    while queue: 
        temp, idx = queue.popleft()
        idx += 1
        if idx < n: # dfs의 경우와 마찬가지로, idx를 하나씩 올려주며 numbers를 탐색
            queue.append([temp+numbers[idx], idx]) # temp를 통해 인덱스의 값을 빼고, 늘리는 
            queue.append([temp-numbers[idx], idx]) # 경우를 탐색
        else:  
            if temp == target: 
                answer += 1
    
    return answer






# def solution(numbers, target): # dfs(재귀) 풀이
#     n = len(numbers)
#     answer = 0
#     def dfs(idx,result):
#         if idx == n: # idx가 n이 됐을시(0부터 시작해서 numbers리스트 전체를 다 탐색했을시)
#             if result == target: #원하는 값이 됐다면 answer에 더해줘야 함
#                 nonlocal answer #바깥함수의 answer를 사용 
#                 answer += 1
#             return
#         else: # idx가 아직 작을때(다 탐색하지 않았을경우)
#             dfs(idx+1,result+numbers[idx]) # 다음idx에 해당하는 numbers[idx]값을 더하고 빼주어서
#             # 더하고 빼는 모든 경우의 수를 탐색해본다
#             dfs(idx+1,result-numbers[idx])
            
#     dfs(0,0)
#     return answer