# def solution(participant, completion): # 정렬 이용한 풀이
#     # O(n)도 허용x?
#     participant = sorted(participant)
#     completion  = sorted(completion)

#     for i in range(len(completion)): 
#         if completion[i] != participant[i]:
#             return participant[i] # 정렬된 리스트 중간에 탈락자가 있는경우
#     return participant[-1] # 마지막에 탈락자가 있는경우
            

def solution(participant, completion): # 해시 이용한 풀이
    dic = {i:0 for i in participant}
    
    for i in participant:
        dic[i] += 1
    
    for j in completion:
        dic[j] -= 1
    
    answer = [k for k,v in dic.items() if v != 0]
    
    return answer[0] 

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))


# 첫 풀이(시간초과)

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     for i in completion:
#         participant.remove(i)
    
#     return participant[0]