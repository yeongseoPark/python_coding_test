from itertools import combinations

def solution(relation): # ㅇ려웠다.......
    combis = []
    for j in range(1,len(relation[0])+1):
        for i in combinations(list(range(len(relation[0]))), j):
            combis.append(i)
    
    row_leng = len(relation) # set 해서 얘랑 길이 비교
    
    possibles = []
    
    for i in combis: # 후보키가 될 수 있는 조합들
        comparable = []
        for j in relation: # relation의 각 로우들
            rows = []
            for k in i: # 후보키 조합 안의 실제 컬럼
                rows.append(j[k])

            rows   = tuple(rows)

            comparable.append(rows)

        
        if len(set(comparable)) == row_leng:
            possibles.append(i)
      
    count  = 0
    dell   = 0
    standard = ""
    
    possibles.sort(key=len)
    
    # [(0,), (0, 3), (1, 2), (1, 2, 3)] 
    
    answer = set(possibles)
    for i in range(len(possibles)):
        for j in range(i+1, len(possibles)):
            if set(possibles[i]).issubset(set(possibles[j])):
                answer.discard(possibles[j]) # 있으면 삭제 없으면 donothing
                    
    return len(answer)

