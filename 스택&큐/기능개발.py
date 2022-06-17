def solution(progresses, speeds): # 큐 사용
    bapor = []
    
    while progresses: # 큐에 원소 존재하는 동안
        for i in range(len(progresses)): # progresses길이 = speeds 길이 
            progresses[i] += speeds[i] # 계속 개발속도만큼 더해나감

        cnt = 0  # 배포한 개수
        while progresses and progresses[0] >= 100: # 큐의 앞에서부터 100넘으면
            # 그런데 만약 앞에서부터 뒤까지 다 100넘은 경우 있을 수 있으므로 while progresses 조건 걸어줌
            # 아니면 index out of range
            progresses.pop(0) # progresses맨앞
            speeds.pop(0)     # speeds 맨앞 제거 
            cnt += 1          # 배포 횟수 += 1

        if cnt > 0: # 배포한 날이면 리스트에 cnt append 
            bapor.append(cnt)
    
    return bapor
        

    

print(solution([93, 30, 55],[1, 30, 5]))