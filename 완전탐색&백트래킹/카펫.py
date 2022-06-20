def solution(brown, yellow):
    dividers = [(i,yellow//i) for i in range(1,yellow+1) if yellow%i == 0]
    # yellow의 약수 구함(튜플로 저장)
    
    for divider in dividers: 
        if (divider[0]+2)*(divider[1]+2)-yellow == brown: # 노랑 가로 +2 * 노랑 세로 +2 - 노랑 개수 = 브라운 개수
            answer = [divider[0]+2, divider[1]+2]  # 전체 가로와 세로 answer에 담음
            sorted(answer, reverse=True)
    
    return answer

print(solution(8,1))