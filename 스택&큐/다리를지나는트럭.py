
# def solution(bridge_length, weight, truck_weights): # 답 보고 품
#     answer = 0
#     bridge = [0] * bridge_length

#     while bridge: 
#         answer += 1
#         bridge.pop(0) # 마지막 대기 트럭까지 다리에 투입되는 순간 bridge 길이 하나씩 줄어든다 

#         if truck_weights: # 트럭 대기줄 있는 동안 if문 수행
#             if sum(bridge) + truck_weights[0] <= weight:  
#                 bridge.append(truck_weights.pop(0))
#             else:
#                 bridge.append(0) # 트럭 대기줄 있는 동안은 위의 pop과 밑의 append들로 길이가 유지 됨

#     return answer


# # def solution(bridge_length, weight, truck_weights): 첫 풀이 21 점
# #     bridge = deque([0] * bridge_length)
    
# #     passed = 0 # 통과한 트럭개수
# #     answer = 0 # 걸린 시간 
    
# #     while passed < len(truck_weights):
# #         answer += 1
        
# #         poped = bridge.pop() # 맨 오른쪽
# #         if poped != 0: 
# #             passed += 1
        
# #         if sum(bridge)+truck_weights[0] <= weight:  # 맨 왼쪽
# #             bridge.appendleft(truck_weights[0])
# #         else:
# #             bridge.appendleft(0)
        
# #         for i in range(len(bridge)-2,-1): # 거꾸로 (뒤 두번째 ~ 맨 앞)
# #             if bridge[i] != 0 and bridge[-1] == 0 :
# #                 bridge[i+1] = next
# #                 bridge[i+1] = bridge[i]
# #                 bridge[i] = next 
                
# #     return answer 
            
# # print(solution(2,10,[7,4,5,6]))
    
        
        
def solution(bridge_length, weight, truck_weights): # 내풀이
    bridge = [0] * bridge_length
    answer = 0    

    while bridge: # bridge가 존재하는 동안 

        while truck_weights: # truck_weight가 존재하는 동안 
            bridge.pop(0) # 왼쪽 popleft() -> deque로 변환하고 popleft()쓰는 코드 빼니깐 시간초과 없앨 수 있었음
            # 굳이 deque쓸필요없이 시간상으로 리스트를 사용해 큐로 처리하는게 더 빠른듯하다

            if sum(bridge)+truck_weights[0] <= weight: # 트럭이 다리위에 올라갈 수 있다면
                a = truck_weights.pop(0) # 대기열에서 빼서 
                bridge.append(a) # 다리에 넣어줌
            else:
                bridge.append(0) # 무게때문에 올라갈수 없다면 그냥 0 append
            
            answer += 1 # 시간 +=1 
        
        bridge.pop(0) 
        answer += 1
    
    return answer
        
print(solution(2, 10, [7, 4, 5, 6]))
            
    