

def solution(clothes):
    # 2차원 배열의 각 요소중 인덱스 1이 카테고리 나타냄
    dic = {}
    answer = 1

    # for i in clothes: # 카테고리 : [해당하는 아이템들] 리스트 만듬 
    #     if i[1] in dic:
    #         dic[i[1]].append(i[0])
    #     else:
    #         dic[i[1]] = [i[0]]

    for i in clothes:
        dic[i[1]] = dic.get(i[1],0) + 1
        ## dic[i[1]] 에 해당하는 값이 없을시, 0으로 기본값 설정한후 1더해주고, 값이 있다면 그 값에 1더해줌
    
    for v in dic.values(): # 경우의 수 문제 
        # 각 카테고리별로 하나씩 고르면 되니, 아이템 갯수+1(안입는 경우) 의 선택지가 있음
        # 이를 카테고리별 선택지들을 다 곱해주면 됨
        answer *= v+1 
    
    return answer-1 # 다만, 모두 안입는 경우는 제외해줘야 하기에 -1 해줌
    
    

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])