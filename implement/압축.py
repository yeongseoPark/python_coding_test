def solution(msg):
    answer = []
    dic = {chr(i+64):i for i in range(1,27)}
    num = 27
    while True:
        brk = False
        
        for i in range(len(msg),-1,-1):
            a = msg[:i]
            
            if a in dic:
                if a == msg: # 사전에 있는 글자가 msg그 자체일때(마지막일때)
                    answer.append(dic[a])
                    brk = True
                    break

                answer.append(dic[a])
                dic[msg[:i+1]] = num
                num += 1
                msg = msg[i:]
                break
                
        if brk:
            break
    
    return answer
            
            