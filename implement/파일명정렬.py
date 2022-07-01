import re


def solution(files):
    for_compare_str = [[v[:re.search(r"\d",v).start()].lower(),i] for i,v in enumerate(files) ]
    # head부터 비교하기 위해서 [문자열,인덱스] 를 리스트에 담음
    for_compare_str.sort(key = lambda x:x[0])
    # 이것을 문자열 기준으로 정렬함

    dic = {}
    for i in for_compare_str:
        dic[i[0]] =[x[1] for x in for_compare_str if x[0] == i[0]]
    # 딕셔너리에 문자열 : [인덱스1, 인덱스2...] 식으로 head와 head같은 인덱스들 담음

    for i in dic:
        if len(dic[i]) > 1: # 만약에 head가 같은 아이들이 여러개라면
            int_compare = [] 
            for k in dic[i]: # img~ 에 해당하는 인덱스들 for문돌림
                start = re.search(r"\d", files[k]).start() # 숫자의 시작
                end   = re.search(r"\D",files[k][start:]).start() + start if re.search(r"\D",files[k][start:]) else len(files[k])
                #숫자의 끝 -> 숫자가 아닌 다른 문자이거나 or 그냥 문자열의 마지막이거나(숫자 담에 암것도 없는경우 re.search()는 None이 된다)

                int_compare.append((k, int(files[k][start:end]))) # int_compare에 (인덱스, 숫자) 형식으로 넣음
            int_compare.sort(key=lambda x: x[1]) # 이를 숫자기준으로 정렬
            
            dic[i] = [h[0] for h in int_compare] # 정렬한 인덱스 리스트 다시 넣음 img: [3,1,2,4] 이런 느낌
    
    answer = []
    for i in dic:
        for j in dic[i]:
            answer.append(files[j])
    
    return answer
                