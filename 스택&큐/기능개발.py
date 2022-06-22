# def solution(progresses, speeds): # 큐 사용 
#     bapor = []
    
#     while progresses: # 큐에 원소 존재하는 동안
#         for i in range(len(progresses)): # progresses길이 = speeds 길이 
#             progresses[i] += speeds[i] # 계속 개발속도만큼 더해나감

#         cnt = 0  # 배포한 개수
#         while progresses and progresses[0] >= 100: # 큐의 앞에서부터 100넘으면
#             # 그런데 만약 앞에서부터 뒤까지 다 100넘은 경우 있을 수 있으므로 while progresses 조건 걸어줌
#             # 아니면 index out of range
#             progresses.pop(0) # progresses맨앞  # pop(0) 사용하여 지워줌
#             speeds.pop(0)     # speeds 맨앞 제거 
#             cnt += 1          # 배포 횟수 += 1

#         if cnt > 0: # 배포한 날이면 리스트에 cnt append 
#             bapor.append(cnt)
    
#     return bapor
        

def solution(progresses, speeds): # 다른 풀이 
    answer = []
    
    while progresses:        
        for i in range(len(progresses)): # 개발 진행
            progresses[i] += speeds[i]

        

        for i in range(len(progresses)-1,-1,-1):  # 뒤에서부터 앞으로 거꾸로 for문 돈다
            if progresses[i] >= 100: # 만약 100점을 넘는 아이가 있으면
                if i == 0: # 근데 그게 첫번째(맨앞)이면
                    answer.append(1) # 얘만 배포하고 끝
                    del progresses[0] # 배포했으니 progresses와 speeds에서 다 지워준다
                    del speeds[0]
                      
                else:  # 100점 넘는 아이가 중간이나 끝에 있으면
                    backward = progresses[:i]  # backward = 처음~그 아이 앞
                    if min(backward) >= 100:   # backward가 다 개발이 끝났으면
                        answer.append(len(backward)+1) # 그만큼 배포했으니 answer에 넣어주고 
                        del progresses[:i+1] # 배포 완료했으니 각각 지워준다 
                        del speeds[:i+1]
                        break # 앞을 지워줬으니 여기서 끝낸다(위에서는 이미 for문의 마지막이니 break필요없다)
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
            
            
            
        
                
                        


                

