def solution(participant, completion):
    # O(n)도 허용x?
    participant = sorted(participant)
    completion  = sorted(completion)

    for i in range(len(completion)): 
        if completion[i] != participant[i]:
            return participant[i] # 정렬된 리스트 중간에 탈락자가 있는경우
    return participant[-1] # 마지막에 탈락자가 있는경우
            
    

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))