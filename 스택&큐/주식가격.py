def solution(prices):
    answer = []
    for i in range(len(prices)):
        if i == len(prices)-1:
            answer.append(0)
            
        cnt = 1
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]: # 가격이 떨어진경우
                answer.append(cnt)
                break
            else: # 가격이 떨어지지 않은 경우 
                if j == len(prices)-1:
                    answer.append(cnt)
                    
                cnt += 1
                
                
    return answer

solution([1,2,3,2,3])