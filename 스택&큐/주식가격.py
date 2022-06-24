# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         if i == len(prices)-1:
#             answer.append(0)
            
#         cnt = 1
#         for j in range(i+1,len(prices)):
#             if prices[i] > prices[j]: # 가격이 떨어진경우
#                 answer.append(cnt)
#                 break
#             else: # 가격이 떨어지지 않은 경우 
#                 if j == len(prices)-1:
#                     answer.append(cnt)
                    
#                 cnt += 1
                
                
#     return answer

# solution([1,2,3,2,3])

def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        if i == len(prices)-1:
            answer.append(0)
        current = prices[i] 
        cnt = 0
        for j in range(i+1,len(prices)):
            cnt += 1
            if prices[j] < current: # 매번 prices[i]로 찾아야 할 필요없게 미리 current변수에 저장
                answer.append(cnt)
                break
            if j == len(prices) -1:
                answer.append(cnt)
    
    return answer
            
