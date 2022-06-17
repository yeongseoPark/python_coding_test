
def solution(bridge_length, weight, truck_weights): # 답 보고 품
    answer = 0
    bridge = [0] * bridge_length

    while bridge: 
        answer += 1
        bridge.pop(0) # 마지막 대기 트럭까지 다리에 투입되는 순간 bridge 길이 하나씩 줄어든다 

        if truck_weights: # 트럭 대기줄 있는 동안 if문 수행
            if sum(bridge) + truck_weights[0] <= weight:  
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0) # 트럭 대기줄 있는 동안은 위의 pop과 밑의 append들로 길이가 유지 됨

    return answer


# def solution(bridge_length, weight, truck_weights): 첫 풀이 21 점
#     bridge = deque([0] * bridge_length)
    
#     passed = 0 # 통과한 트럭개수
#     answer = 0 # 걸린 시간 
    
#     while passed < len(truck_weights):
#         answer += 1
        
#         poped = bridge.pop() # 맨 오른쪽
#         if poped != 0: 
#             passed += 1
        
#         if sum(bridge)+truck_weights[0] <= weight:  # 맨 왼쪽
#             bridge.appendleft(truck_weights[0])
#         else:
#             bridge.appendleft(0)
        
#         for i in range(len(bridge)-2,-1): # 거꾸로 (뒤 두번째 ~ 맨 앞)
#             if bridge[i] != 0 and bridge[-1] == 0 :
#                 bridge[i+1] = next
#                 bridge[i+1] = bridge[i]
#                 bridge[i] = next 
                
#     return answer 
            
# print(solution(2,10,[7,4,5,6]))
    
        
        
        
        
        
        
            
    